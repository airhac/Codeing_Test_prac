def solution(m, musicinfos):
    answer = []
    ch1 = ['C#', 'D#', 'F#', 'G#', 'A#']
    ch2 = ['c', 'd', 'f', 'g', 'a']
    for c1, c2 in zip(ch1, ch2):
        m = m.replace(c1, c2)

    for index, music in enumerate(musicinfos):
        start, end, name, music_info = music.split(',')
        s_h, s_m = map(int, start.split(':'))
        e_h, e_m = map(int, end.split(':'))

        play_time = (e_h * 60 + e_m) - (s_h * 60 + s_m)
        for c1, c2 in zip(ch1, ch2):
            music_info = music_info.replace(c1, c2)
        if len(music_info) > play_time:
            temp = music_info[:play_time]
        else:
            a = play_time // len(music_info)
            b = play_time % len(music_info)
            temp = music_info * a + music_info[:b]
        if m in temp:
            answer.append((play_time, index,  name))

    if len(answer) == 1:
        return answer[0][2]
    elif len(answer) > 1:
        answer = sorted(answer, key=lambda x: (-x[0] , x[1]))
        return answer[0][2]
    else:
        return "(None)"