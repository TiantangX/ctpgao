from sdk.gaoapi2 import GaoApi
print(1)
api=GaoApi("086515","123456")
print(2)
行情=api.获取_K线("SHFE.rb2101",10)
api.获取_tick("SHFE.rb2101")
while True:
    api.wait_update()
    持仓=api.查持仓("SHFE.rb2101")
    print(持仓)