# -*- coding: utf-8 -*-


ori_text = r"""
\begin{equation}
	a^{s_L} = 
		\left(\begin{matrix}
			a_1^{(s_L)(1)} & a_2^{(s_L)(1)} & a_3^{(s_L)(1)} & \dots & a_{s_L}^{(s_L)(1)} \\
			a_1^{(s_L)(2)} & a_2^{(s_L)(2)} & a_3^{(s_L)(2)} & \dots & a_{s_L}^{(s_L)(2)} \\
			a_1^{(s_L)(3)} & a_2^{(s_L)(3)} & a_3^{(s_L)(3)} & \dots & a_{s_L}^{(s_L)(3)} \\
			\vdots & \vdots & \vdots & \ddots & \vdots \\
			a_1^{(s_L)(m)} & a_2^{(s_L)(m)} & a_3^{(s_L)(m)} & \dots & a_{s_L}^{(s_L)(m)} \\
		\end{matrix}\right)
\end{equation}
"""

old = 'a_'
new = 'z_'


def replace(ori_text, old, new):
	return ori_text.replace(old, new)


if __name__ == '__main__':
	des_text = replace(ori_text, old, new)
	print(des_text)