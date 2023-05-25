zip_list = [30605, 30216, 30214, 30215, 54822, 30213]
zip_list_1 = [30605,  30215, 54822]
uniques = []

for a in zip_list_1:
    for b in zip_list:
        if a == b:
           # uniques.append(a)
           zip_list.remove(a)

print(f"This is mutual {zip_list}")

#if delete the warehouse than the zip code of the warehouse will be appended to the zip list which makes that zip code available for testing




#  Scenario: Checking all links are working fine
#      Then I verify rad link is working fine
#      And I verify rad learn more link is working fine
#      Then I verify lift gate link is working fine
#      Then I verify lift gate learn more link is working fine
#      Then I verify quote freight direct link is working fine
#      Then I verify quote freight direct services link is working fine
#      Then I verify shipping slug link is working fine




#    Then I verify that dropship locations are available on product page

