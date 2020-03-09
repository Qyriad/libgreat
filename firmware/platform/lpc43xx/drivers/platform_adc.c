/*
 * This file is part of libgreat
 *
 * LPC43xx ADC functions
 */

#include <toolchain.h>

#include <drivers/adc.h>
#include <drivers/platform_adc.h>
#include <drivers/timer.h>
#include <debug.h>

platform_adc_registers_t *platform_get_adc_registers()
{
	// ADC base address.
	return (platform_adc_registers_t *) 0x400E3000;
}

int platform_adc_init(adc_t *adc)
{
	// Select ADC0 FIXME: don't do this
	adc->reg->adc_select = 1;

	// Select operating mode.
	adc->reg->power_enabled = 1;

	return 0;
}

uint16_t adc_blocking_get_value(adc_t *adc)
{
	uint32_t start_time = get_time();

	adc->reg->start_trigger = ADC_START_NOW;

	while (!adc->reg->done) {
		if (get_time_since(start_time) > (3 * 1000000UL)) {
			pr_error("Timed out waiting for ADC conversion to complete!\n");
			break;
		}
	}

	return adc->reg->voltage;
}
