<template>
	<div class="toast-wrapper">
		<div ref="el" class="toast">
			{{ text }}
		</div>
	</div>

</template>

<script>
import gsap from 'gsap'
import { onMounted, onUnmounted, ref } from 'vue';
export default {
	props: [
		'text',
	],
	setup(props, { emit }) {
		const el = ref(null)


		onMounted(() => {
			let duration = 0.3
			gsap.fromTo(el.value, {
				opacity: 0,
				y: -100
			}, {
				opacity: 1,
				y: 0,
				duration: duration
			})
			setTimeout(() => {
				gsap.to(el.value, {
					keyframes: [
						{ x: 8 },
						{ x: -8 },
						{ x: 4 },
						{ x: -4 },
						{ x: 0 },
					],
					duration: 0.2
				})
			}, duration * 1000)
		})

		setTimeout(() => {
			let duration = 0.3
			gsap.to(el.value, {
				opacity: 0,
				y: -100,
				duration: duration
			})
			setTimeout(() => {
				emit('close')
			}, duration * 1000);
		}, 3000)
		return {
			el
		}
	}
}
</script>

<style>
.toast-wrapper {
	position: fixed;
	z-index: 999;
	left: 50%;
	top: 0;
	transform: translateX(-50%);
}

.toast {
	background-color: rgb(255, 118, 140);
	padding: 20px 80px;
	border-radius: 20px;
	margin-top: 20px;
	color: white;
	font-size: 1.2em;
	cursor: default;
}
</style>