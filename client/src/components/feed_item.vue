<template>
  <div class="pb-3">
    <div
      class="card-body feed-html-container"
      v-html="entry.content['#text']"
    />
    <div v-if="error" class="text-danger ml-3">{{ error }}</div>
    <div v-if="!hideReadLater" class="p-3">
      <button
        type="button"
        class="btn btn-primary float-right read-later-button"
        :disabled="loading"
        @click="readLater"
      >
        <span v-if="!loading">Read Later</span>
        <span
          v-else
          class="spinner-grow spinner-grow-sm"
          role="status"
          aria-hidden="true"
        ></span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeedItem',
  data() {
    return {
      loading: false,
      error: null,
    }
  },
  props: {
    entry: {
      type: Object,
      required: true,
    },
  },
  computed: {
    hideReadLater() {
      return this.$route.name === 'feed-read_later'
    },
  },
  methods: {
    async readLater() {
      try {
        this.loading = true
        await this.$store.dispatch('setReadLater', {
          handle: this.$route.params.feed,
          entryId: this.entry.id,
        })
      } catch {
        this.error = 'Request Failed'
      } finally {
        this.loading = false
      }
    },
  },
}
</script>

<style scoped>
.read-later-button {
  width: 12rem;
}
</style>

<style scoped>
.feed-html-container {
  padding-bottom: 0 !important;
}
</style>
