def solution(id_list, report, k):
    report_dict = {}
    cnt_dict = {}
    
    for i in id_list:
        report_dict[i] = []
        cnt_dict[i] = 0

    for r in report:
        a, b = r.split()
        if a not in report_dict[b]:
            report_dict[b].append(a)
    
    for i in id_list:
        if len(report_dict[i]) >= k:
            for j in report_dict[i]:
                cnt_dict[j] += 1

    answer = []
    for i in id_list:
        answer.append(cnt_dict[i])

    return answer