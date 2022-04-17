from rest_framework.views import APIView


lst = [
    {
        "id": 21,
        "author": "Иванов",
        "content": "Коммент Иванова на статью 1",
        "id_kor": 0,
        "level": 1,
        "post_id": 5,
    },
    {
        "id": 22,
        "author": "Петров",
        "content": "Коммент Петрова на статью 1",
        "id_kor": 21,
        "level": 2,
        "post_id": 5,
    },
    {
        "id": 23,
        "author": "Сидоров",
        "content": "Коммент Сидорова статью 1",
        "id_kor": 22,
        "level": 3,
        "post_id": 5,
    },
    {
        "id": 24,
        "author": "Кузнецов",
        "content": "Коммент Кузнецова статью 1",
        "id_kor": 23,
        "level": 4,
        "post_id": 5,
    },
    {
        "id": 25,
        "author": "Моисеев",
        "content": "Коммент Моисеева на статью 1",
        "id_kor": 24,
        "level": 5,
        "post_id": 5,
    },
    {
        "id": 26,
        "author": "Васюков",
        "content": "Коммент Васюкова на статью 1",
        "id_kor": 21,
        "level": 2,
        "post_id": 5,
    },
    {
        "id": 27,
        "author": "Калганов",
        "content": "Коммент Калганова на статью 1",
        "id_kor": 0,
        "level": 1,
        "post_id": 5,
    },
    {
        "id": 28,
        "author": "Бутусов",
        "content": "Коммент Бутусова на статью 2",
        "id_kor": 0,
        "level": 1,
        "post_id": 6,
    },
    {
        "id": 29,
        "author": "Климов",
        "content": "Коммент Климова на Бутусова на статью 2",
        "id_kor": 28,
        "level": 1,
        "post_id": 6,
    },
    {
        "id": 30,
        "author": "Зимин",
        "content": "Коммент Зимина на статью 2",
        "id_kor": 22,
        "level": 3,
        "post_id": 5,
    },
]


# def struc(lst):
#     structure = {}
#     for item in lst:
#         if item["id_kor"] == 0 and ('Статья' + str(item["post_id"])) not in structure:
#             structure.update({'Статья' + str(item["post_id"]): [item["id"]]})
#         elif item["id_kor"] == 0 and ('Статья' + str(item["post_id"])) in structure:
#             structure['Статья' + str(item["post_id"])].append(item["id"])
#         else:
#             if item["id_kor"] not in structure:
#                 structure.update({item["id_kor"]: [item["id"]]})
#             else:
#                 structure[item['id_kor']].append(item["id"])
#     print(structure)
#     return structure


# gr = struc(lst)
# print(gr)
# {'Статья5': [21, 27], 21: [22, 26], 22: [23], 23: [24], 24: [25], 'Статья6': [28, 30], 28: [29]}
# gr = {21: [22, 26]}


class Nnn(APIView):
    pass


class Dada:

    @staticmethod
    def struc(lst):
        structure = {}
        for item in lst:
            if item["id_kor"] == 0 and ('Статья' + str(item["post_id"])) not in structure:
                structure.update({'Статья' + str(item["post_id"]): [item["id"]]})
            elif item["id_kor"] == 0 and ('Статья' + str(item["post_id"])) in structure:
                structure['Статья' + str(item["post_id"])].append(item["id"])
            else:
                if item["id_kor"] not in structure:
                    structure.update({item["id_kor"]: [item["id"]]})
                else:
                    structure[item['id_kor']].append(item["id"])
        print(structure)
        return structure

    @staticmethod
    def dfs1(graph, start, visited=None):
        if visited is None:
            visited = {}
            visited.update({start: {}})

        for node in graph[start]:
            if node in graph:
                visited[start].update({node: {}})
                Dada.dfs1(graph, node, visited[start])
            else:
                visited[start].update({node: None})
        return visited


gr = Dada.struc(lst)
# gr = {21: [22, 26]}
xx = Dada.dfs1(gr, 21)
print(xx)
