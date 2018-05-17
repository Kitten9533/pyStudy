class yourLib(object):  
	# ROBOT_LIBRARY_SCOPE = 'TEST CASE'
	# ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    # ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    # TEST CASE：在每个test case中引用都会实例化一次
    # TEST SUITE：在suite中引用，只会实例化一次，也就是说10个test case都引用了这个类的方法，但是只有第一个test case是调用的时候实例化，后续的共用
    # GLOBAL：在全局只实例化一次，调用一次后，在所有suite中引用、test case中引用都不会再实例化

    def __init__(self, member=None):  
        self.members = [member] if member else []  
  
    def add_member(self, name):  
        self.members.append(name)  
        return self.members