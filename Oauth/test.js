const options = {
	authProvider,
};

const client = Client.init(options);

let search = await client.api('/me/drive/root/search(q='finance')?select=name,id,webUrl')
	.get();