
class Cart:
    # 초기화 메서드
    def __init__(self):
        self.items = []  #장바구니 비어있음

    # 아이템 추가 메서드
    def add_item(self, item):
        self.items.append(item)

    # 아이템 조회(검색) 메서드
    def get_items(self):
        return f"장바구니: {self.items}"

    # 아이템 제거 메서드
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

# main 영역에서만 실행됨
if __name__ == "__main__":
    cart = Cart()
    cart.add_item("여름바지")
    cart.add_item("양말")
    cart.add_item("손수건")
    # 아이템 삭제
    cart.remove_item("양말")
    cart.remove_item("반팔티") # 품목에 없음
    # 아이템 조회
    print(cart.get_items())