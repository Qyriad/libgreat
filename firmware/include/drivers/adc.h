/*
 * This file is part of libgreat
 *
 * Generic DAC driver header.
 */

#ifndef __LIBGREAT_ADC_H__
#define __LIBGREAT_ADC_H__

#include <toolchain.h>
#include <drivers/platform_adc.h>

typedef struct adc {
	platform_adc_registers_t *reg;
} adc_t;


int adc_init(adc_t *adc);

#endif
