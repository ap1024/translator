# translator
（一个中英文翻译小工具）a Chinese and English translation tools in the terminal and based on [Youdao translation api](http://ai.youdao.com/docs/api.s.)

# Install

git clone https://github.com/sikasjc/translator.git

sudo mv ./translator.py /usr/local/bin/tr

sudo chmod +x /usr/local/bin/tr

# Usage

### Modify the value of the appKey and key.

tr [word]

    >>> tr python

    ----------translation----------
    
    python: python
    
    ----------basic explain----------
    
    n. 巨蟒；大蟒 n. （法）皮东（人名）
    
    ----------web explain----------
    
    python: 蟒蛇,Python,蟒属 Burmese Python: 缅甸蟒,缅甸蟒,黄金蟒 Python regius: 球蟒,球蟒
    ---------------------------------

tr [sentence] 
    
    >>> tr I like walking

    ----------translation----------
    
    I like walking: 我喜欢步行
    
    ----------basic explain----------
    
    
    ----------web explain----------
    
    I like walking: 我喜欢散步,我喜欢散步.
    I Felt Like Walking: 我觉得喜欢走路 
    I suddenly feel like walking: 我忽然想走着去
    ---------------------------------
    
### change language
open translator.py and modify *translatefrom and *translateto

语言	| 代码
---- | ---
中文	| zh-CHS
日文	| ja
英文	| EN
韩文	| ko
法文	| fr
俄文	| ru
葡萄牙文 |	pt
西班牙文	| es
