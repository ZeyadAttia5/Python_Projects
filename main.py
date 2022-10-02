with open("C:/Users/Administrator/Desktop/DIO/DIO.h", "w+") as DIO_Header:
	DIO_Header.write('/*\n')

	DIO_Header.write(' * Dio.h\n')

	DIO_Header.write(' *\n')

	DIO_Header.write(' *  Created on: Sep 2, 2022\n')

	DIO_Header.write(' *      Author: Administrator\n')

	DIO_Header.write(' */\n')

	DIO_Header.write('#ifndef INCLUDE_MCAL_DIO_DIO_H_\n')

	DIO_Header.write('#define INCLUDE_MCAL_DIO_DIO_H_\n')

	DIO_Header.write('\n')

	DIO_Header.write('#include "../../../SERVICES/STD_TYPES.h"\n')

	DIO_Header.write('\n')

	DIO_Header.write('typedef enum{\n')

	DIO_Header.write('		DIO_enuOk,\n')

	DIO_Header.write('		DIO_invalidInput\n')

	DIO_Header.write('}DIO_tenuErrorStatus;\n')

	DIO_Header.write('\n')

	DIO_Header.write('/*Port Define */\n')

	DIO_Header.write('#define DIO_u8_PORTA 0\n')

	DIO_Header.write('#define DIO_u8_PORTB 1\n')

	DIO_Header.write('#define DIO_u8_PORTC 2\n')

	DIO_Header.write('#define DIO_u8_PORTD 3\n')

	DIO_Header.write('\n')

	DIO_Header.write('/* PIN Define */\n')

	DIO_Header.write('#define DIO_u8_PIN0 0\n')

	DIO_Header.write('#define DIO_u8_PIN1 1\n')

	DIO_Header.write('#define DIO_u8_PIN2 2\n')

	DIO_Header.write('#define DIO_u8_PIN3 3\n')

	DIO_Header.write('#define DIO_u8_PIN4 4\n')

	DIO_Header.write('#define DIO_u8_PIN5 5\n')

	DIO_Header.write('#define DIO_u8_PIN6 6\n')

	DIO_Header.write('#define DIO_u8_PIN7 7\n')

	DIO_Header.write('\n')

	DIO_Header.write('/* PIN DIRECTIONS */\n')

	DIO_Header.write('#define DIO_u8_INPUT 0\n')

	DIO_Header.write('#define DIO_u8_OUTPUT 1\n')

	DIO_Header.write('\n')

	DIO_Header.write('/* Pin Value Options */\n')

	DIO_Header.write('#define DIO_u8_HIGH 0x01\n')

	DIO_Header.write('#define DIO_u8_LOW 0x00\n')

	DIO_Header.write('\n')

	DIO_Header.write('/* Port Direction */\n')

	DIO_Header.write('#define DIO_u8_PORT_INPUT 0\n')

	DIO_Header.write('#define DIO_u8_PORT_OUTPUT 255\n')

	DIO_Header.write('\n')

	DIO_Header.write('/* IO Pins */\n')

	DIO_Header.write('\n')

	DIO_Header.write('DIO_tenuErrorStatus DIO_eunSetPinValue(u8 Copy_u8PortId, u8 Copy_u8PinId, u8 Copy_u8PinVal);\n')

	DIO_Header.write('\n')

	DIO_Header.write('u8 DIO_u8GetPinValue(u8 Copy_u8PortId, u8 Copy_u8PinId);\n')

	DIO_Header.write('\n')

	DIO_Header.write('DIO_tenuErrorStatus DIO_enuSetPinDirection(u8 Copy_u8PortId, u8 Copy_u8PinId, u8 Copy_u8PinDir);\n')

	DIO_Header.write('\n')

	DIO_Header.write('/* IO Ports */\n')

	DIO_Header.write('DIO_tenuErrorStatus DIO_enuSetPortDirection(u8 Copy_u8PortId, u8 Copy_u8PinDir);\n')

	DIO_Header.write('\n')

	DIO_Header.write('DIO_tenuErrorStatus DIO_enuSetPortValue(u8 Copy_u8PortId, u8 Copy_u8PortVal); //Output Direction Only\n')

	DIO_Header.write('\n')

	DIO_Header.write('\n')

	DIO_Header.write('DIO_tenuErrorStatus DIO_enuTogglePinValue(u8 Copy_u8PortId, u8 Copy_u8PinId);\n')

	DIO_Header.write('\n')

	DIO_Header.write('#endif /* INCLUDE_MCAL_DIO_DIO_H_ */\n')

with open("C:/Users/Administrator/Desktop/DIO/DIO_prv.h", "w+") as DIO_prv:

	DIO_prv.write('/*\n)')

	DIO_prv.write(' * Dio_prv.h\n)')

	DIO_prv.write(' *\n)')

	DIO_prv.write(' *  Created on: Sep 2, 2022\n)')

	DIO_prv.write(' *      Author: Administrator\n)')

	DIO_prv.write(' */\n)')

	DIO_prv.write('\n)')

	DIO_prv.write('#ifndef INCLUDE_MCAL_DIO_DIO_PRV_H_\n)')

	DIO_prv.write('#define INCLUDE_MCAL_DIO_DIO_PRV_H_\n)')

	DIO_prv.write('\n)')

	DIO_prv.write('#define DDRA_REGISTER *((volatile u8*) 0x3A)\n)')

	DIO_prv.write('#define PORTA_REGISTER *((volatile u8*) 0x3B)\n)')

	DIO_prv.write('#define PINA_REGISTER *((volatile u8*) 0x39)\n)')

	DIO_prv.write('\n)')

	DIO_prv.write('#define DDRB_REGISTER *((volatile u8*) 0x37)\n)')

	DIO_prv.write('#define PORTB_REGISTER *((volatile u8*) 0x38)\n)')

	DIO_prv.write('#define PINB_REGISTER *((volatile u8*) 0x36)\n)')

	DIO_prv.write('\n)')

	DIO_prv.write('#define DDRC_REGISTER *((volatile u8*) 0x34)\n)')

	DIO_prv.write('#define PORTC_REGISTER *((volatile u8*) 0x35)\n)')

	DIO_prv.write('#define PINC_REGISTER *((volatile u8*) 0x33)\n)')

	DIO_prv.write('\n)')

	DIO_prv.write('#define DDRD_REGISTER *((volatile u8*) 0x31)\n)')

	DIO_prv.write('#define PORTD_REGISTER *((volatile u8*) 0x32)\n)')

	DIO_prv.write('#define PIND_REGISTER *((volatile u8*) 0x30)\n)')

	DIO_prv.write('\n)')

	DIO_prv.write('#endif /* INCLUDE_MCAL_DIO_DIO_PRV_H_ */\n)')
