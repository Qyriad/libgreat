/*
 * This file is part of libgreat
 *
 * LPC43xx ADC functions.
 */


#ifndef __LIBGREAT_PLATFORM_ADC_H__
#define __LIBGREAT_PLATFORM_ADC_H__

#include <toolchain.h>


typedef struct adc adc_t;


/**
 * Structure representing the in-memory layout of an ADC data register
 */
typedef volatile struct ATTR_PACKED platform_adc_data_register {
	uint32_t /*reserved*/ :  6;
	uint32_t voltage      : 10;
	uint32_t /*reserved*/ : 14;
	uint32_t overrun      :  1;
	uint32_t done         :  1;
} platform_adc_data_register_t;


typedef enum start {
	ADC_NO_START = 0x00,
	ADC_START_NOW,
	ADC_START_EDGE_START0,
	ADC_START_EDGE_START1,
	ADC_START_EDGE_START2,
	ADC_START_EDGE_START3,
	ADC_START_EDGE_START4,
	ADC_START_EDGE_START5,
} adc_start_t;


/**
 * Structure representing the in-memory layout of an ADC peripheral.
 */
typedef volatile struct ATTR_PACKED platform_adc_registers {
	union {
		struct {
			uint32_t adc_select         : 8;
			uint32_t clock_divider      : 8;
			uint32_t burst_mode_enabled : 1;
			uint32_t clock_select       : 3;
			uint32_t /*reserved*/       : 1;
			uint32_t power_enabled      : 1;
			uint32_t /*reserved*/       : 2;
			uint32_t start_trigger      : 3;
			uint32_t use_falling_edge   : 1;
			uint32_t /*reserved*/       : 4;
		};
		uint32_t control_register;
	};

	union {
		struct {
			uint32_t /*reserved*/   :  6;
			uint32_t voltage        : 10;
			uint32_t /*reserved*/   :  7;
			uint32_t channel_number :  3;
			uint32_t /*reserved*/   :  3;
			uint32_t overrun        :  1;
			uint32_t done           :  1;
		};
		uint32_t global_data_register;
	};

	RESERVED_WORDS(1);

	union {
		struct {
			uint32_t enable_interrupts            :  8;
			uint32_t enable_global_done_interrupt :  1;
			uint32_t /*reserved*/                 : 23;
		};
		uint32_t interrupt_enable_register;
	};

	platform_adc_data_register_t data_registers[8]; // Channels 0-7

	union {
		struct {
			uint32_t status_done    :  8;
			uint32_t status_overrun :  8;
			uint32_t interrupt_flag :  1;
			uint32_t /*reserved*/   : 15;
		};
		uint32_t status_register;
	};
} platform_adc_registers_t;

ASSERT_OFFSET(platform_adc_registers_t, global_data_register, 0x004);
ASSERT_OFFSET(platform_adc_registers_t, interrupt_enable_register, 0x00C);
ASSERT_OFFSET(platform_adc_registers_t, status_register, 0x030);

platform_adc_registers_t *platform_get_adc_registers();
int platform_adc_init(adc_t *adc);
uint16_t adc_blocking_get_value(adc_t *adc);

#endif
