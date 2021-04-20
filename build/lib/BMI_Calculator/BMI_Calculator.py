import pandas as pd
df=pd.read_json('testcase.json',lines=True)
df[['BMI_value','BMI_Category','Health_Risk']]= ''

def formula_1(mass,height):
    if height==0:
        return 'NaN','invalid_data','invalid_data'
    height=height/100
    bmi= round(mass/(height*height),1)
    if bmi<=18.4: return bmi,'Underweight','Malnutrition Risk'
    elif 18.5<=bmi<=24.9: return bmi,'Normal weight','Low risk'
    elif 25<=bmi<=29.9: return bmi,'Overweight','Enhanced risk'
    elif 30<=bmi<=34.9: return bmi,'Moderately obese','Medium risk'
    elif 35<=bmi<=39.9: return bmi,'Severely obese','High risk'
    elif bmi>=40: return bmi,'Very severely obese','Very high risk'
    

df[['BMI_value','BMI_Category','Health_Risk']]=list(map(formula_1, df['WeightKg'],df['HeightCm']))

df.to_json('output.json',orient="index")