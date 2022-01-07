def solution(gems):
    answer = []
    shortest = len(gems) + 1

    start_p = 0
    end_p = 0

    len_total_gem = len(set(gems))
    contained_gem = {}

    while end_p < len(gems):
        if gems[end_p] not in contained_gem:
            contained_gem[gems[end_p]] = 1
        else:
            contained_gem[gems[end_p]] += 1
        
        end_p += 1

        if len(contained_gem) == len_total_gem:
            while start_p < end_p:
                if contained_gem[gems[start_p]] > 1:
                    contained_gem[gems[start_p]] -= 1
                    start_p += 1
                elif shortest > end_p - start_p:
                    shortest = end_p - start_p
                    answer = [start_p+1, end_p]
                    break
                else:
                    break

    return answer
