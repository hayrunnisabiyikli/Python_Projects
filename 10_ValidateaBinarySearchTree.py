class BinaryTree:
    def __init__(self, val, leftnode=None, rightnode=None):
        self.val = val
        self.leftnode = leftnode
        self.rightnode = rightnode
"""
leftnode ve rightnode özellikleri ile sol ve sağ 
alt ağaçları ifade eden diğer ikili ağaç düğümlerini tutar.
"""

class BinarySearchTree:
    def validate_BST(self, root: BinaryTree) -> bool:
        return self.valid(root, float('inf'), float('-inf'))

    def valid(self, root, max_val, min_val):
        if root is None:
            return True

        # Kontrol edilecek geçerlilik koşulları buraya eklenebilir

        return (
            min_val < root.val < max_val
            and self.valid(root.leftnode, root.val, min_val)
            and self.valid(root.rightnode, max_val, root.val)
        )

# Örnek kullanım, İkili arama ağacını oluştur
tree = BinaryTree(
    10,
    BinaryTree(5),
    BinaryTree(
        15,
        BinaryTree(13),
        BinaryTree(20)
    )
)

"""
       10
      /  \
     5    15
         /  \
        13   20
oluşturduğumuz binary tree
"""

# BinarySearchTree sınıfını kullanarak geçerlilik doğrulaması yap
bst = BinarySearchTree()
is_valid = bst.validate_BST(tree)
print(is_valid)  # True veya False olarak çıktı verir

"""
validate_BST yöntemi, geçerlilik doğrulamasını yapmak için kullanılır. Bu yöntem, valid yöntemine geçerli 
kök düğümü, bir maksimum değer (max_val) ve bir minimum değer (min_val) parametresi olarak geçirir.

valid yöntemi, verilen kök düğümün geçerlilik kontrolünü gerçekleştirir. Öncelikle, kök düğümünün 
None olup olmadığı kontrol edilir. Eğer None ise, bu durumda bir geçerlilik hatası yoktur ve True döndürülür.

Aksi takdirde, kök düğümünün değeri (root.val) ve 
maksimum/minimum değerler (max_val ve min_val) arasında geçerlilik kontrolü yapılır. Ardından, valid yöntemi sol alt ağaç ve sağ alt ağaç için rekürsif olarak çağırılır, uygun maksimum ve minimum değerler güncellenir.
"""