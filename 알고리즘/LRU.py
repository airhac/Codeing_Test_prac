class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
        
class DoublyLinkedList:
    def __init__(self, cachSize):
        self.cacheSize = cachSize
        self.head = Node("")
        self.tail = Node("")
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def LRU(self, data):
        print("[Put " + data + "]", end=" ")
        node = self.head.next
        while(node.data):
            if node.data == data:
                self.cacheHit(node, data)
                return 1
            node = node.next
        self.cacheMiss(data)#data가 node에 같은 데이터가 없으면 이 함수를 실행
        return 5
    def cacheHit(self, node, data):
        self.removeNode(node)
        self.addFront(data)
        print("Hit", end=" ")
        self.printAll()
    
    def removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    def addFront(self, data):
        newNode = Node(data)
        self.head.next.prev = newNode
        newNode.next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
    # 원소의 맨앞에 추가(cacheSize가 보다 커지면 tail에 가까운 node를 삭제)    
    def cacheMiss(self, data):
        self.addFront(data)
        if self.cacheSize < self.totalLen():
            self.removeTail()
        print("Miss", end=" ")
        self.printAll()
            
    def totalLen(self):
        answer = 0
        node = self.head.next
        while (node.data):
            answer += 1
            node = node.next
        return answer
      
    def removeTail(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
    # For Debug  
    # head 부터 tail 까지 순환하면서 date 전부 출력
    
    def printAll(self):
        node = self.head.next
        while(node.data):
            print(node.data, end="")
            node = node.next
            if (node.data):
                print(" -> ", end="")
        print()
inputArray = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
test = DoublyLinkedList(3)
answer = 0
for input in inputArray:
    answer += test.LRU(input)
print(answer)