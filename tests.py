# dictionary of tests, one for each function in the project spec; in each case, list a number of function calls (as a str), and the correct output for each
tests = {
    "swap_cards":[
        ("submission.swap_cards(['JS', 'QD', 'KC', '7S', '9H', '4C', '0C', '9C', '5H', '3C', 'JH', '2H', '8D'],3)",[['JS', 'QD'], ['JS', 'KC'], ['JS', '7S'], ['JS', '9H'], ['JS', '4C'], ['JS', '0C'], ['JS', '9C'], ['JS', '5H'], ['JS', '3C'], ['JS', 'JH'], ['JS', '2H'], ['JS', '8D'], ['QD', 'KC'], ['QD', '7S'], ['QD', '9H'], ['QD', '4C'], ['QD', '0C'], ['QD', '9C'], ['QD', '5H'], ['QD', '3C'], ['QD', 'JH'], ['QD', '2H'], ['QD', '8D'], ['KC', '7S'], ['KC', '9H'], ['KC', '4C'], ['KC', '0C'], ['KC', '9C'], ['KC', '5H'], ['KC', '3C'], ['KC', 'JH'], ['KC', '2H'], ['KC', '8D'], ['7S', '9H'], ['7S', '4C'], ['7S', '0C'], ['7S', '9C'], ['7S', '5H'], ['7S', '3C'], ['7S', 'JH'], ['7S', '2H'], ['7S', '8D'], ['9H', '4C'], ['9H', '0C'], ['9H', '9C'], ['9H', '5H'], ['9H', '3C'], ['9H', 'JH'], ['9H', '2H'], ['9H', '8D'], ['4C', '0C'], ['4C', '9C'], ['4C', '5H'], ['4C', '3C'], ['4C', 'JH'], ['4C', '2H'], ['4C', '8D'], ['0C', '9C'], ['0C', '5H'], ['0C', '3C'], ['0C', 'JH'], ['0C', '2H'], ['0C', '8D'], ['9C', '5H'], ['9C', '3C'], ['9C', 'JH'], ['9C', '2H'], ['9C', '8D'], ['5H', '3C'], ['5H', 'JH'], ['5H', '2H'], ['5H', '8D'], ['3C', 'JH'], ['3C', '2H'], ['3C', '8D'], ['JH', '2H'], ['JH', '8D'], ['2H', '8D']]),
        ("submission.swap_cards(['QD', 'QH', '8S', '9D', '7S', '3S', 'AD', '0C', '8C', '3H', 'JS', '5D', 'AH'],0)",[['AH','AD']]),
        ("submission.swap_cards(['QD', 'QH', '8S', '9D', '7S', '3S', 'AD', '0C', '8C', '3H', 'JS', '5D', 'AH'],1)",[['AD'],['AH']]),
        ("submission.swap_cards(['3C', '4S', '5C', '5D', '9H', '0D', '5H', '0H', 'KS', '9C', '8S', 'KC', '2S'],2)",[['3C'], ['4S'], ['5C'], ['5D'], ['9H'], ['0D'], ['5H'], ['0H'], ['KS'], ['9C'], ['8S'], ['KC'], ['2S']]),
        ],

    "generate_plays":[
        ('submission.generate_plays(["3D", "4D", "4C", "5D", "JS", "JC"])', [ ["3D"], ["4D"], ["4C"], ["5D"], ["JS"], ["JC"], ["4D", "4C"], ["JS", "JC"], ["3D", "4D", "5D"] ]),
        ('submission.generate_plays(["3H", "5D", "5S", "7C", "7D", "2S", "2C"])', [['3H'], ['2S'], ['2C'], ['2S', '2C'], ['5D'], ['5S'], ['5D', '5S'], ['7C'], ['7D'], ['7C', '7D']]),
        ('submission.generate_plays(["2H", "3H", "4H", "5H", "6H", "7H", "8H"])', [['3H'], ['4H'], ['5H'], ['6H'], ['7H'], ['8H'], ['2H'], ['3H', '4H', '5H', '6H', '7H', '8H'], ['3H', '4H', '5H', '6H', '7H'], ['3H', '4H', '5H', '6H'], ['3H', '4H', '5H'], ['4H', '5H', '6H', '7H', '8H'], ['4H', '5H', '6H', '7H'], ['4H', '5H', '6H'], ['5H', '6H', '7H', '8H'], ['5H', '6H', '7H'], ['6H', '7H', '8H']]),
        ('submission.generate_plays(["2H", "AH", "KH", "QH", "JH", "0H", "9H"])', [['9H'], ['0H'], ['JH'], ['QH'], ['KH'], ['AH'], ['2H'], ['9H', '0H', 'JH', 'QH', 'KH', 'AH', '2H'], ['9H', '0H', 'JH', 'QH', 'KH', 'AH'], ['9H', '0H', 'JH', 'QH', 'KH'], ['9H', '0H', 'JH', 'QH'], ['9H', '0H', 'JH'], ['0H', 'JH', 'QH', 'KH', 'AH', '2H'], ['0H', 'JH', 'QH', 'KH', 'AH'], ['0H', 'JH', 'QH', 'KH'], ['0H', 'JH', 'QH'], ['JH', 'QH', 'KH', 'AH', '2H'], ['JH', 'QH', 'KH', 'AH'], ['JH', 'QH', 'KH'], ['QH', 'KH', 'AH', '2H'], ['QH', 'KH', 'AH'], ['KH', 'AH', '2H']]),
        ('submission.generate_plays(["2S", "3C", "4H", "5D", "6S", "7C", "8H"])', [['3C'], ['2S'], ['5D'], ['4H'], ['7C'], ['6S'], ['8H']]),
        ('submission.generate_plays(["3S", "3C", "3H", "3D", "4D", "5D", "6D"])', [['3S'], ['3C'], ['3H'], ['3D'], ['3S', '3C'], ['3S', '3H'], ['3S', '3D'], ['3C', '3H'], ['3C', '3D'], ['3H', '3D'], ['3S', '3C', '3H'], ['3S', '3C', '3D'], ['3S', '3H', '3D'], ['3C', '3H', '3D'], ['3S', '3C', '3H', '3D'], ['5D'], ['4D'], ['6D'], ['3D', '4D', '5D'], ['4D', '5D', '6D'], ['3D', '4D', '5D', '6D']]),
        ],

    "is_valid_play":[
        ('submission.is_valid_play(["2C"], [["KD"]])',True),
        ('submission.is_valid_play(None, [])',False),
        ('submission.is_valid_play(["AD"], [["5S", "5C"],["6H", "6C"]])',False),
        ('submission.is_valid_play(["4D", "5D", "6D", "7D", "8D"],[["5H", "6H", "7H"], None])',True),
        ('submission.is_valid_play(["4D", "5D", "6D", "8D", "7D"],[["6H", "5H", "7H"], None])',True),
        ('submission.is_valid_play(["4D", "5D", "6D", "8D", "7D"],[["7H", "5H", "6H"], None])',True),
        ('submission.is_valid_play(None,[["5H", "6H", "7H"], None])',True),
        ('submission.is_valid_play(["8H", "9H", "0H"], [["5H", "6H", "7H"], None, ["4D", "5D", "6D", "7D", "8D"]])',True),
        ('submission.is_valid_play(["8H", "6H", "7H"], [["5H", "6H", "7H"], None, ["4D", "5D", "6D", "7D", "8D"]])',False),
        ('submission.is_valid_play(["0H", "9H", "8H"], [["6H", "5H", "7H"], None, ["4D", "8D", "6D", "7D", "5D"]])',True),
        ('submission.is_valid_play(["QH", "KH", "AH"], [["5H", "6H", "7H"], None, ["9H", "0H", "JH"]])',True),
        ('submission.is_valid_play(["QC", "KC", "AC"], [["5H", "6H", "7H"], None, ["9H", "0H", "JH"]])',False),
        ('submission.is_valid_play(["QC","KC","AC"], [["0S", "JS", "QS"]])',True),
        ],

    "play":[
        ("submission.play([], ['JS', 'QD', 'KC', '7S', '9H', '4C', '0C', '9C', '5H', '3C', 'JH', '2H', '8D'], [[]], [13,13,13,13])", [['3C'], ['4C'], ['5H'], ['7S'], ['8D'], ['9H'], ['9C'], ['9H', '9C'], ['0C'], ['JS'], ['JH'], ['JS', 'JH'], ['QD'], ['KC'], ['2H']]),
        ("submission.play([['3D']], ['JS', 'QD', 'KC', '7S', '9H', '4C', '0C', '9C', '5H', '3C', 'JH', '2H', '8D'], [[['3D']]], [12,13,13,13])", [['4C'], ['5H'], ['7S'], ['8D'], ['9H'], ['9C'], ['0C'], ['JS'], ['JH'], ['QD'], ['KC'], ['2H']]),
        ],

        }

