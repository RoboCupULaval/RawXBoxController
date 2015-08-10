/*
 * Robocup_Define.h
 *
 *  Created on: 2013-10-16
 *      Author: Mathieu Garon
 */

#ifndef ROBOCUP_DEFINE_H_
#define ROBOCUP_DEFINE_H_

#include <stdio.h>

#include <stdbool.h>
#include <stdint.h>

typedef _Bool bool_t;

#define NUMBER_OF_PLAYER 6
#define PLAYER_BUFFER_SIZE 15
#define CIRCULARBUFFER_SIZE 256


/****************************************************************************
 * 								Circular Buffer
 ****************************************************************************/
struct CB_Handle{

	uint8_t byteCount;
	bool_t dataReady;
	uint16_t dataBuffer[CIRCULARBUFFER_SIZE];
	uint16_t dataBufferCursorRead;
	uint16_t dataBufferCursorWrite;

};

typedef struct CB_Handle CB_Handle;

/****************************************************************************
 * 								unpacker
 * 	Each Players have a buffer. packetSize is the actual number of data in that
 * 	buffer
 ****************************************************************************/
#define STARTBYTE 0x7E
#define ESCAPEBYTE 0x7D
#define STOPBYTE 0x7F
#define NO_PLAYER_SET -1
typedef struct UnPacker_Handle{

	uint16_t playerBuffer[NUMBER_OF_PLAYER][PLAYER_BUFFER_SIZE];
	bool playerReady[NUMBER_OF_PLAYER];

	uint16_t byteCount;
	int16_t currentPlayertoTransfer;
	bool isParsing;
	bool escapeNextByte;

}UnPacker_Handle;


#define HandleRF  HandleRobot.HandleRF
#define HandleSerial  HandleRobot.HandleSerial


#endif /* ROBOCUP_DEFINE_H_ */
