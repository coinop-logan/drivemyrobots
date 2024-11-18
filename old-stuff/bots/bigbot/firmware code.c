/*
0 - 0xff (header)
1 - 0xfe (header)
2 - leftVal
3 - leftVal
4 - rightVal
5 - rightVal
6 - sum of bytes 0-5
7 - sum of bytes 0-5
*/



for (int tmp = 0; tmp < sizeof(command_tmp) - 7; tmp++) {

	if (command_tmp[tmp] == 0xff && command_tmp[tmp + 1] == 0xfe) {

		uint16_t sumget = (uint16_t) command_tmp[tmp + 6] << 8 | (uint16_t) command_tmp[tmp + 7];

		uint16_t sumcheck = 0;
		for (int tmp_2 = 0; tmp_2 < 6; tmp_2++) {
			sumcheck += command_tmp[tmp + tmp_2];
		}

		if (sumget == sumcheck) {			
			// -1000 - 1000
			leftVal = ((int16_t) command_tmp[tmp + 2]) << 8 | (int16_t) command_tmp[tmp + 3];
			rightVal = ((int16_t) command_tmp[tmp + 4]) << 8 | (int16_t) command_tmp[tmp + 5];
			break;
		}

	}

}
