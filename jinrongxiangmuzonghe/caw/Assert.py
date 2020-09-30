'''
断言公共方法
'''
import pytest_check as check


class Assert:
    def equal(self,expect,response,key_skr):
        '''

        :return:
        '''
        try:
            keys=key_skr.split(',')
            for key in keys:
                r=str(response[key])
                e=expect[key]
                check.equal(r,e)
                print(f"响应信息为：{response},预期结果为{expect},校验字段：{key},实际结果：{r},预期结果：{e},建校成功")
        except Exception as e:
            print(f"响应信息为：{response},预期结果为{expect},校验字段：{key},实际结果：{r},预期结果：{e},建校失败")

