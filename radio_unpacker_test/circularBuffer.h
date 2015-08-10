/*
 * circularBuffer.h
 *
 *  Created on: 2014-05-23
 *      Author: Dominic Bilodeau
 */

#ifndef CIRCULARBUFFER_H_
#define CIRCULARBUFFER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "Robocup_Define_RadioBase.h"

CB_Handle CB_init();

bool CB_write(CB_Handle *circularBuffer, uint16_t pByte);
bool CB_read(CB_Handle *circularBuffer, uint16_t *pByte);
void CB_flush(CB_Handle *circularBuffer);
void CB_print(CB_Handle *circularBuffer);

#ifdef __cplusplus
}
#endif

#endif /* CIRCULARBUFFER_H_ */
