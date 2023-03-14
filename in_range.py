def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """
    
    # stri = str(nums)            - my attempt was over-thinking
    # strLow = str(lowest)
    # strHigh = str(highest)
    # maximum = max(nums)
    # minimum = min(nums)
    # print(minimum)
    # # print(maximum)
    # print(stri.__contains__('40'))
    # print(list(range(lowest, highest + 1)))

    # if stri.__contains__(strLow) and stri.__contains__(strHigh):
    #   print(f"{lowest} fits")
    #   print(f"{highest} fits")
    # elif stri.__contains__(strLow):
    #   print(lowest, 'lowest value')
    # elif stri.__contains__(strHigh):
    #   print(strHigh, 'highest value')
    # elif highest > maximum and lowest < minimum:
    #   print(minimum)
    #   print(maximum)
    # else:
      
      # for 

        

      # find closest number
      
# vegan_no_nos = ['eggs', 'meat', 'milk' ,'fish', 'figs']
# # to try and check if some ingredient is in vegan_no_nos:
# pie_ingredients = ['flour','apples','sugar', 'eggs', 'salt']
# # ^ want to check pie_ingredients to see if any of these ingredients are non-vegan
# for food in pie_ingredients:
#     if food in vegan_no_nos:
#         print(f"gosh darn it no, cannot eat {food}, it is not vegan!")
#     else:
#         print(f"yum, I love {food}")

       

        
     
      # for n in enumerate(nums):
      #     print(n)

      
      

      # print('ok')
    # for n in nums:
      
    # YOUR CODE HERE
    
   
      
    # print(stri.__contains__('20'))

# in_range([10, 20, 30, 40, 50], 15, 30)  
# in_range([10, 20, 30, 40, 50], 5, 100)  
# in_range([10, 20, 30, 40, 50], 20, 30)
in_range([10, 20, 30, 40, 50], 15, 45)  





# Python string __contains__()

def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    for num in nums:
        if num >= lowest and num <= highest:
            print(f"{num} fits")


in_range([10, 20, 30, 40, 50], 15, 30)            
