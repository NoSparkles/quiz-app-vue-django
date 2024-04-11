<template>
    <div class="question-navigation">
        <ul>
            <li v-for="(item, index) in Array(numOfQuestions)" @click="handleClick(index)"
                :style="{ backgroundColor: current === index ? 'rgb(18, 255, 97)' : '' }">{{ index + 1
                }}</li>
        </ul>
    </div>
</template>

<script>

import { } from 'vue'
export default {

    setup(props, { emit }) {

        const handleClick = (index) => {
            emit('changeQuestion', index)
        }
        return {
            handleClick
        }
    },
    props: [
        'numOfQuestions',
        'current'
    ]
}
</script>

<style>
.question-navigation {
    margin: auto;
    margin-top: 50px;
    width: 60%;

}

.question-navigation ul {
    list-style: none;
    display: flex;
    gap: 20px;
    overflow-x: scroll;
}


.question-navigation ul li {
    height: 40px;
    width: 40px;
    border-radius: 20px;
    background-color: rgb(80, 147, 248);
    display: flex;
    color: white;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    font-weight: 700;
}
</style>