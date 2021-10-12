<template>
    <ul class="project-list">
        <ProjectCard v-for="project in projects" :key="project.id" :project="project" />
    </ul>
</template>

<script>
import ProjectCard from '@/components/ProjectCard.vue'
import data from '@/data.js'

export default {
    data() {
        return {
            projects: data.projects,
        }
    },
    components: {
        ProjectCard,
    },
}
</script>

<style lang="scss">
    .project-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, auto));
        justify-content: center;
        justify-items: center;
        gap: 40px;
    }
</style>