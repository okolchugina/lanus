get-mac:
	hcitool dev | grep -o "[[:xdigit:]:]\{11,17\}"