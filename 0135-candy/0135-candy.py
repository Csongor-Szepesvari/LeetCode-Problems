class Solution:
    def candy(self, ratings: List[int]) -> int:
        num_candies = 0
        last_candy = 0
        last_rating = 0
        trend_up = True
        trend_length = 0
        buffer = 0
        for i in range(len(ratings)):
            
            rating = ratings[i]
            #print("rating is", rating, "last_rating is", last_rating)
            #print("last candy is", last_candy)
            #print("buffer", buffer)
            if rating == last_rating:
                num_candies += 1
                last_candy = 1
                buffer = 1
                trend_length = 1
                trend_up = False
            elif rating < last_rating:
                #print("going down")
                # we're trending down
                if trend_up:
                    #switch from going up to going down
                    if last_candy > 1:
                        num_candies += 1
                        buffer = last_candy
                    else:
                        num_candies += 2
                        buffer = last_candy + 1
                    last_candy = 1
                    trend_length = 2
                else:
                    #trend down continues, if we can't go down then we need to increase all the last ones

                    trend_length += 1
                    if trend_length > buffer:
                        num_candies += trend_length
                    else:
                        num_candies += trend_length - 1
                    last_candy = 1

                trend_up = False

        
            elif rating > last_rating:
                #we're going up, so we have to increase based on the last candy
                #print("going up")
                trend_up = True
                last_candy += 1
                num_candies += last_candy

            #print("on step", i+1, "currently total candies is", num_candies)
            #print()
            last_rating = rating

        return num_candies
