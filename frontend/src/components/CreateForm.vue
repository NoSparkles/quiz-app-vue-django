<template>
    <div class="form-wrapper">
        <form>
            <input type="text" ref="title" placeholder="Title">
            <ul class="questions">
                <li v-for="(question, qIndex) in questions" :key="qIndex">
                    <label>{{ qIndex + 1 }}.</label>
                    <input type="text" placeholder="">
                    <ul class="answers">
                        <li>
                            <label>{{ qIndex + 1 }}.</label>
                            <input type="text" placeholder="">
                        </li>
                    </ul>
                </li>
            </ul>
        </form>
    </div>
</template>

<script>
import { ref } from 'vue'
export default {
    setup() {
        const title = ref('')
        const questions = ref([
            {
                question: '',
                answers: [
                    '',
                    ''
                ]
            },
        ])



        return {
            title,
            questions
        }
    }
}
</script>

<style></style>