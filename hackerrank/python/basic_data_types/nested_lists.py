if __name__ == '__main__':
    name_scores = []
    for i in range(int(input())):       # gakusei no ru-pu
        name = input()                  # namae
        score = float(input())          # tensuu
        name_scores.append([name, score])    # risutoni tsuikasuru
        
# sukoa dake chuushutsu, set()de juufuku o haijoshte, sorted()de so-to shi 2banmeno atai[1] o dainyu

second_score = sorted(set([score for name, score in name_scores]))[1]

second_score_name = "\n".join(sorted([name for name, score in name_scores if score == second_score]))

print(second_score_name)

