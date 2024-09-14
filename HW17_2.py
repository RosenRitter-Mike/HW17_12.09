import sqlite3
import pandas as pd
import sqlite_lib as sl
import pprint


df = pd.read_csv('E-commerce Customer Behavior - Sheet1.csv');
conn = sqlite3.connect('e_commerce.db');
df.to_sql('e_commerce', conn, if_exists='replace', index=False);


conn.commit()
conn.close()

# ================================================================================

sl.connect('e_commerce');
cus_num = sl.run_query_select('SELECT COUNT(*) FROM e_commerce');
print(f"- The number of customers is: {cus_num[0][0]}");
cus_age = sl.run_query_select('SELECT AVG(Age) FROM e_commerce');
print(f"- The average age of customers is: {cus_age[0][0]:.2f}");
gen_num = sl.run_query_select('SELECT Gender, COUNT(*) FROM e_commerce ec GROUP BY Gender');
print(f"- {gen_num[0][0]} customers number:{gen_num[0][1]}\n- {gen_num[1][0]} customers number:{gen_num[1][1]}");
gen_buy = sl.run_query_select('SELECT Gender, AVG("Items Purchased") FROM e_commerce ec GROUP BY Gender');
print(f"- {gen_buy[0][0]} customers average items purchased:{gen_buy[0][1]}\n"
      f"- {gen_buy[1][0]} customers average items purchased:{gen_buy[1][1]}");
mem_types = sl.run_query_select('SELECT COUNT(DISTINCT "Membership Type") FROM e_commerce ec');
print(f"- There are {mem_types[0][0]} types of memberships");
mem_num = sl.run_query_select('SELECT "Membership Type", COUNT(*) FROM e_commerce ec GROUP BY "Membership Type";')
print(f"- There are: \n {mem_num[0][1]} {mem_num[0][0]} customers\n"\
                f" {mem_num[1][1]} {mem_num[1][0]} customers\n"\
                f" {mem_num[2][1]} {mem_num[2][0]} customers");
ny_cus = sl.run_query_select('SELECT City, COUNT(*) FROM e_commerce ec WHERE City = "New York"');
print(f"- There are {ny_cus[0][1]} customers from {ny_cus[0][0]}");
ct_cus = sl.run_query_select('SELECT City, COUNT(*) cus_cnt FROM e_commerce ec GROUP BY City ORDER BY cus_cnt DESC');
print("- Customers grouped by city in descending order:");
for city in ct_cus:
    print(f"  There are {city[1]} customers from {city[0]}");
gen_spend = sl.run_query_select('SELECT Gender, SUM("Total Spend") FROM e_commerce ec GROUP BY Gender');
print(f"- {gen_spend[0][0]} customers spent {gen_spend[0][1]:.2f} in total\n"
      f"- {gen_spend[1][0]} customers spent {gen_spend[1][1]:.2f} in total");

max_cus = sl.run_query_select('SELECT "Customer ID" FROM e_commerce ec WHERE "Items Purchased" = '
                              '(SELECT MAX("Items Purchased") FROM e_commerce);');
print('- The customers who purchased the most items (21 items) are:')
for customer in max_cus:
    print(f'  {customer[0]}', end=", ");

print();
min_cus = sl.run_query_select('SELECT "Customer ID" FROM e_commerce ec WHERE "Items Purchased" = '
                              '(SELECT MIN("Items Purchased") FROM e_commerce);');
print('- The customers who purchased the least items (7 items) are:')
for customer in min_cus:
    print(f'  {customer[0]}', end=", ");