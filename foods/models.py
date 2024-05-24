from django.db import models

class  Food(models.Model):
    name = models.CharField(max_length= 200)
    kcal = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return self.name + ' ' + self.kcal + ' 大卡' + ' {' + self.description + '}'
    
# 创建一个新的 MyModel 实例并手动设置 id 为 0
new_instance = Food(id=0, name="肉粽", kcal="200~300", description="肉粽是一種傳統的中國食物，主要由糯米、豬肉、鹹蛋黃、香料等材料製成，然後用竹葉包裹，再蒸煮而成。肉粽通常是一種營養豐富的食物，但是其熱量會根據製作方法和具體配料而有所不同。")
new_instance.save()
