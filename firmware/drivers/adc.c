/*
 * This file is part of libgreat
 *
 * Generic ADC driver.
 */

#include <toolchain.h>
#include <drivers/adc.h>
#include <drivers/platform_adc.h>

int adc_init(adc_t *adc)
{
	adc->reg = platform_get_adc_registers();

	int rc = platform_adc_init(adc);
	if (rc) {
		return rc;
	}

	return 0;
}
