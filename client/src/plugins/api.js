import Vue from 'vue'

export class API {
  endpointUrl = 'https://wycxhkur4i.execute-api.af-south-1.amazonaws.com/dev/'

  async fetchFeed(githubHandle, readLater = false) {
    const data = { handle: githubHandle, read_later: readLater }
    const response = await fetch(this.endpointUrl + 'feed', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    return response.json()
  }

  async addToReadLater(githubHandle, entryId) {
    const data = { handle: githubHandle, entry_id: entryId }
    const response = await fetch(this.endpointUrl + 'read-later', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    return response.json()
  }
}

const api = new API()
Vue.$api = api
Vue.prototype.$api = api
