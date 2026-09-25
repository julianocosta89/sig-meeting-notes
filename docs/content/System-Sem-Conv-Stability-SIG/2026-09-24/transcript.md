SIG: System Sem Conv Stability SIG
Date: 2026-09-24
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin (Splunk Inc.)** 00:17 Hi, Christos.
**Christos Markou** 00:23 Hello?
**Roger** 00:29 8.
**Pablo Baeyens** 00:58 Great.
**Braydon Kains (Google LLC)** 01:09 Hi, sorry I'm late, I had a computer problem.
**Dmitrii Anoshin (Splunk Inc.)** 01:16 Do you folks are going to keep going?
**Roger** 01:23 Yeah, I think Christos and myself are going…
**Dmitrii Anoshin (Splunk Inc.)** 01:28 Nice. Pablo Braydon will also be there, right?
**Pablo Baeyens** 01:31 At Gibcon? No, I won't be… I won't be there.
**Braydon Kains (Google LLC)** 01:36 I will be there, keep coming.
**Dmitrii Anoshin (Splunk Inc.)** 01:37 Okay, cool.
Cool.
It'll be good to see you, folks.
I'll be there as well.
**Pablo Baeyens** 01:44 You can put a small photo of me or something to, like…
**Braydon Kains (Google LLC)** 01:47 We'll Photoshop you in.
**Pablo Baeyens** 01:49 Right.
**Braydon Kains (Google LLC)** 01:51 Your little GitHub avatar will Photoshop it in on the side.
**Pablo Baeyens** 01:54 You know, it's enough.
**Braydon Kains (Google LLC)** 01:57 Yeah.
If you want to get up at whatever ungodly hour early in the morning, we can Zoom you into the collector dinner.
**Pablo Baeyens** 02:09 You can certainly send me a message on Slack, yeah, so you know…
**Braydon Kains (Google LLC)** 02:21 Looks like we don't have Donald, but his PR that he mentioned got merged anyway.
So… There's probably not much to talk about.
Which means, I suppose we can go to the fun part.
Now, can I share my screen? That's the question. I've never tried this on the new laptop before.
Chrome tab? I can share a Chrome tab, right?
Okay, so… this… came up… I mean, this has been a thing for a long time, but it came up internally, and prompted me to, like, start actually looking into it. So, some of it is… some of this is, like, restated from problems that Roger already knew and talked about, but… Essentially, the issue right now is that the… System memory usage metric.
Well, after looking into it, I realized it was always wrong, like, it always didn't sum to the proper memory total that we thought it should, but it's now even more wrong, because… GoPS Util adopted the more accurate calculation for the used state. Well, what we use for the used state, the value that we use, is now the more accurate mem total minus mem available on Linux.
But because of the way MAMAvailable is calculated, if you use that in… A sum across all the states on On the memory available metric, it's even more not mem total.
So… We basically need to decide, like.
Are we go… do we need… what do we need to change about system memory usage if we really want that sum?
to be correct.
we can… make… The used state alone Less correct by doing the proper Math.
Based on the other states.
Or, we can change the memory usage metric to only have two states for used and available, where used is total minus available, and then available is just Available.
And then for the rest of the states, introduce Either make them opt-in metrics and let users know that if you… opt-in attributes, and if you opt into them, your sum will not be meaningful. The sum across all dimensions won't be meaningful.
Or we introduce them as other… Other opt-in metrics entirely.
I… I think that is essentially this… the summary of… of the dilemma we have right now. I did look into how… Node Exporter and Telegraph. Those are the two I looked at for, like, how they handle this sort of thing, and the answer is that they don't. Node Exporter just kind of exposes the raw values from PROCFS in their own metrics, all in separate time series, so they don't care about this, like, sum across dimensions is the total, or anything like that. They just expose the raw values from PROCFS, and Telegraph Has a memory usage metric, and the dimensions on that metric are just entirely different depending on the… platform used, and they do not sum to a meaningful value. They're just, like, raw counters from ProcFS on Linux, and equivalents in other systems. So, we're the only environment that I can see, the only monitoring environment that has this particular problem.
**Dmitrii Anoshin (Splunk Inc.)** 06:05 Braydon, the potential fixed number one is it has the state that we used to have before, right? Exactly, always doubled in some form.
**Braydon Kains (Google LLC)** 06:14 So, it is sort of the state we had before, but the… Do I mention it in… The difference is that we need to get the cached state like, directly from ProcFS, instead of using the one from GoPS Util.
Cause they… inadvertently, like, as a side effect, they add Slap Reclaimable onto the value you get for cached. So…
**Dmitrii Anoshin (Splunk Inc.)** 06:41 That's it.
**Braydon Kains (Google LLC)** 06:41 We have to do something to circumvent that and get the cash value ourselves, and we have to… For our used state, manually also subtract unreclaimable.
So if we… if we do that, then… then the sum will sum to mem total. And the downside is that the used state is not exactly super accurate, I guess.
**Dmitrii Anoshin (Splunk Inc.)** 07:08 Makes sense. And, you mentioned that we might have opt-in attribute. I'm not sure, is this something we currently support?
I don't think so, right?
**Braydon Kains (Google LLC)** 07:22 Can't remember how this works with the mDataGen opt-in attributes feature, and whether it would be.
**Dmitrii Anoshin (Splunk Inc.)** 07:27 Yeah, we can… we can enable, disable, and make, Key is optional, but not the values.
**Braydon Kains (Google LLC)** 07:37 Oh, yeah, true.
So then, it would need to be, like, a… A feature gate or a config field.
Something like that, to, like, produce all the extra value. So it would be kind of… we wouldn't be using a standard mechanism for that, we'd have to introduce our own.
**Dmitrii Anoshin (Splunk Inc.)** 07:55 Unless we want the standard mechanism for something else as well, so keep it generically applicable.
Or something else.
**Braydon Kains (Google LLC)** 08:03 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 08:03 But I'm afraid that it'll be… A little bit more complicated.
**Braydon Kains (Google LLC)** 08:10 it'd be kind of awkward, especially because I think the enum… For this metric, when you… produce it on Windows is just… is, like, a totally different enum anyway, because that whole slab on reclaimable, reclaimable thing isn't, like, the same con. They don't use a… Windows doesn't use a slab allocator at all, I don't think. I can't remember, but…
**Dmitrii Anoshin (Splunk Inc.)** 08:26 Yep.
**Pablo Baeyens** 08:33 I'm sorry, this… Breakage from the way things happened before.
How long ago did it happen? How many versions ago did it happen?
It was a year ago.
Okay.
So, so then… Prior to a year ago, it was… Broken in some odd way about it.
**Braydon Kains (Google LLC)** 08:58 It was…
**Pablo Baeyens** 08:59 So it had been that way for a long time, and now it's broken in a different way.
Since a year ago.
**Braydon Kains (Google LLC)** 09:05 Yeah, I guess it's, like, it's more broken than it used to be. It was already broken before, because… because of the way the math worked, and the way GoPS Util gave us the cached value, S recreclaimable and S unreclaimable were both double counted, so the entire slab was… was double counted, meaning that if you summed citizens.memory usage before across all states, you would already get an overestimation.
Like, you'd overcount from memory total, and now you will overcount further, because memory available is a bit more specific about what it considers available.
Where it considers parts of the page cache, parts of the low watermark, And… some other part. Basically, stuff… Will be considered available more than it used to be, and that means the used value ends up being low… Sorry, math is… is… Screwed me up.
the… The MEM available is usually considered higher than the old formula, And so that means used… will be… lower, because total subtracted by a bigger value… yes, okay. So… Oh man, talking about math is screwing me up. When I write it out, it makes sense, but… Anyways… I think… I think it's… the… the result is there's a bigger delta above… Memory total when you sum now than it used to be.
**Roger** 10:47 The background is that this formula that we compute from other states was… An approximation formula that… used to do, like, the free command a long time ago, and… because, let's say, that the kernel didn't expose a specific metric, they just provided some states, like the free buffer sketch, and the guys that were doing the free command, they said, okay, maybe if we subtract these states, we get a good approximation of what the memory use can be, because the kernel was not exposing nothing.
And they use that formula, but since 10 years ago or more, in the kernel, you have the memory available.
And they added exactly for this specific reason, because, the user space, had these formulas, that they were not accurate. And they decided to add a specific field, and that would be, let's say, the… the API from the user programs to get that value.
And this is the memory available. And actually, the difference in the formula, I think it's not negligible, because for all the tests that I did in the past.
The delta, it's 6-7% all the time, so it's quite a lot.
Mmm… And basically, well, my concern is that Why should we use the old formula if… Let's say the kernel tells us that it's not, The way to compute the used memory.
And there's this big gap between the old one and the new one. In my opinion, we should fix… How, let's say, this assumption about summing the states, not, Not, creating a formula that fits the… This, assumption.
Because there's a lot of other states in the… in the meminfo file.
there's, I don't know, like, well, you have plenty of fields there.
So, I think, yeah, my other proposal, or the other proposal is what Braydon said, just… make, the two default attributes used unavailable and somehow exposed all the other Rakuten for, attributes as other memory states that need to be opt-in by the user, and that they want some to the… to the total.
**Dmitrii Anoshin (Splunk Inc.)** 13:30 You can also expose them in a separate metric, potentially. Or separate metrics.
**Roger** 13:37 - That would be…
**Braydon Kains (Google LLC)** 13:40 Yeah, I kind of lean more towards that one, too, mainly because the system memory usage metric has lots of states that could be useful to some people, but I think a vast majority of users only care about used, like the used state, and then do calculations for utilization or alerts based on on… Calculating utilization using the used state.
At least that's my experience watching users use our synthesis of the same metric in our Ops Agent product?
**Pablo Baeyens** 14:15 Do you… I don't know if you can answer this on a recorded meeting, but, like, do you know if internally people use the other… the queries with the other fields?
the other…
**Braydon Kains (Google LLC)** 14:27 I…
**Pablo Baeyens** 14:29 Polly, you said I should be…
**Braydon Kains (Google LLC)** 14:30 I might be able to look at… if… if Googlers use our…
**Pablo Baeyens** 14:36 Right, yeah, that's what.
**Braydon Kains (Google LLC)** 14:37 Yeah, I might be able to get that data privately and… and figure out the answer. I am not… I'm not sure, is… is… is the…
**Pablo Baeyens** 14:49 Yeah, cause I guess, like… That option of, like, supposing those as separate metrics sounds reasonable to me.
My worry is more like… There may be a… non-negligible percentage of people that did not notice this, and do not care about this, and… We may be breaking them, and so, like.
I don't know, I would feel more comfortable if I knew, like, most people are not using those attributes, and, well, we're not going to know that In general, but… We could try and get info from What we know of.
users that we are close to, I guess.
**Roger** 15:38 At least on our side, we just use the used state, for sure. The used and the available, not the… At least on the default dashboards or integrations that we provide for system, etc, we don't use the… debuffered or cuts. This is more, let's say.
Specific, or you need to query it yourself, not… Not those.
**Pablo Baeyens** 16:01 Right, yeah.
Yeah, and I'm guessing that you either do the query where you join by all the attribute values, which would continue to work here, or you… UTS used, you know.
**Roger** 16:16 Yep.
**Braydon Kains (Google LLC)** 16:17 Another thing I should… I should check is we don't… we don't have any control or ownership over, like.
the Google Compute Engine's hypervisor metrics, but I'm wondering What sort of metrics the hypervisor provides for for GCE, and, like, what sort of dashboards they provide, that might give us some information, too, because if… for Linux VMs, they don't… they give dashboards that don't directly consider any of those other states, either. That's another, potentially.
Interesting point of data.
But I will see what information I can actually gather for what people are using for our metric.
I don't know how to do that, I'll have to ask some people, but I should privately be able to look at that data and then synthesize an answer for us.
Right, yeah.
**Pablo Baeyens** 17:05 We don't need to know.
**Braydon Kains (Google LLC)** 17:06 Yeah, I don't think anyone really cares, anyway.
I will say the reason that that sparked me to start looking at this was… Essentially someone asking about… That metric and asking if we can add the available state.
To the metric.
Because they need to calculate available memory or utilization based on it.
And that was when… when I was going to say.
The used state already has that, so you should sum the states and do a utilization check based on that.
And then there was the whole rabbit hole of, like, oh, actually, the sum is totally wrong, so you can't do what I want to suggest.
That was the reason this can of worms opened for me.
**Roger** 18:09 And the other thing that we need to fix is the catch stage, right?
**Braydon Kains (Google LLC)** 18:15 Yeah.
**Roger** 18:16 now comes from GoP as Utils, already… Sumped with the ZRA Climbal.
And if we expose this row, Well, we need to think if we continue to use GoPsutil in the host metric receiver, or we use another library.
**Dmitrii Anoshin (Splunk Inc.)** 18:40 How do we get as reclaimable? Isn't it from God?
**Braydon Kains (Google LLC)** 18:43 We also get it. We actually could do our own math in host metrics receiver, like, take whatever cache we get back and manually subtract as reclaimable. That is viable.
**Dmitrii Anoshin (Splunk Inc.)** 18:54 Right.
I think I would avoid to… I have introduced in the… parser.
**Braydon Kains (Google LLC)** 19:03 We also may be able to leverage, prometheus has a ProcFS library, so if it really came to that, we might be able to lean on that if we really directly need ProcFS values. For fixing cache, I don't think we do immediately, but… Worth noting that we can probably get around it if we need to in the future.
**Dmitrii Anoshin (Splunk Inc.)** 19:22 By the way, why go past utility in goods as reclaimable and exposing that separately? Isn't this something We can submit an issue about.
**Braydon Kains (Google LLC)** 19:34 So, someone did.
And it led to them documenting their reasoning, but not changing the behavior.
**Dmitrii Anoshin (Splunk Inc.)** 19:42 behavior.
**Braydon Kains (Google LLC)** 19:43 That's the commit where they added the documentation.
And the reason they do it is because free actually does it. Like, if you run free-h, the value you get in the cached column includes SREclaimable.
**Dmitrii Anoshin (Splunk Inc.)** 19:56 Hmm. Oh, I see.
**Braydon Kains (Google LLC)** 19:58 whether that is a justifiable reason for GoPS Util is probably subjective. I would lean on maybe they shouldn't have done that, but…
**Dmitrii Anoshin (Splunk Inc.)** 20:09 Yeah, as long as we… like… Hmm… keep track of that assumption, we can just do the opposite on our side, I guess.
**Braydon Kains (Google LLC)** 20:21 Yeah, I think… independently of everything in the gist, we probably could just make that change uncached, because, like, even… I don't even… I don't think that was ever our intention for system memory usage anyway, and we just never really… thought about it before. I never really thought about the fact that GoPS Util mutates cached for us in a way that we didn't want to, so… I might just submit an issue to change that regardless.
I think… that's good for… for this topic, then. The action item for me is to check What?
Queries people might be doing internally that might rely on these states.
To maybe see if there is a use case for keeping them around on the metric versus producing them as separate metrics for the people who do really care.
My… my instinct is to say that majority of people care about the used state, specifically And not the individual states, and only, like.
really deep Linux sysadmins probably care about those other ones and would be okay with them as separate metrics. That's… that's… that's based on… on nothing, pure conjecture. That's just what I… that's what I think.
**Dmitrii Anoshin (Splunk Inc.)** 22:02 Sounds good. Thank you, Freda.
**Braydon Kains (Google LLC)** 22:06 If we don't have any other topics, I just wanted to bring up one thing just related to the host metrics receiver.
I'm… something that… I was looking at how the Hotel Arrow Collector implemented their host metrics collection.
And one thing they did that I think is really interesting, and I might want to try and bring into the host metrics receiver here, is they… take… they have the same sort of concept as us in Node Exporter, where it's, like, individual scrapers for the different types of things, but… They allow each one to have its own independent scrape interval.
And then in the root of the receiver, they group common intervals together. So, like, if a few of them have 15 seconds as an interval.
They do those scrapes all at once, and then there's, like, a group of that are on 60 seconds, or a group that are on 5 minutes. And it probably wouldn't be that difficult for us to introduce something similar, where we basically spawn A new scraper controller at each… like, unique interval we detect and group the ones that are the same together. The reason I was thinking about this is because what a lot of people do, I've seen in random issues and stuff, where people will make, like, 5 host metrics receiver instances just so they can configure different intervals for the different scrapers, and that's kind of obnoxious in terms of config.
And I'd like to just, kind of.
Solve it directly in the receiver.
So, unless anybody has, like, a direct objection here, I'm gonna open an issue about that, too.
**Dmitrii Anoshin (Splunk Inc.)** 23:40 It's not new, Braydon. There has been an issue for that, and there was some work that tried to implement that. I was reviewing that, actually.
Didn't go far.
It wasn't worse. Okay. I guess there are some, maybe, complications that… Were not addressed from my request on the review or something like that, so it wasn't complete.
And it's not straightforward, that's what I remember, but also I didn't get enough, kind of… Probably.
I would say not… not enough.
engagement from the author in terms of, like, understanding all the edge cases. That's how I would put it.
**Braydon Kains (Google LLC)** 24:29 Okay, I'll see if I can find… find that, and see if there's something I'm missing.
**Dmitrii Anoshin (Splunk Inc.)** 24:36 Yeah, I can send you… I'll try to find Swell and Sem too. But, yeah, it's… My point is that… I'm not… I'm not saying we shouldn't do that or anything like that. My point is that if you do it, it would… it would have much… higher chance, rather than someone who is not familiar with the water.
**Braydon Kains (Google LLC)** 25:02 Yep.
Makes sense.
I think that's everything I had.
**Dmitrii Anoshin (Splunk Inc.)** 25:22 Thank you. Thanks, Fox.
**Braydon Kains (Google LLC)** 25:24 Thanks, everyone.
**Dmitrii Anoshin (Splunk Inc.)** 25:25 Same thing, right?
