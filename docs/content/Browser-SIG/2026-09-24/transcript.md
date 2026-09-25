SIG: Browser SIG
Date: 2026-09-24
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:12 Everyone.
Just waiting a little bit more, maybe, like, one more minute.
Some people are joining.
Okay, it seems like maybe this is gonna be it. Like, there are a few people who can't attend today.
Yeah, so we have only two things on the agenda. Mine is actually pretty short. Jared is just asking for a review. If anyone has anything else that's on their mind, please add it to the agenda.
I can briefly talk about my topic.
Let's see, let me share my screen… But I was hoping for more people to join today to talk about this, but maybe I can… Bring it to next week as well.
But essentially… We have… This… this PR open to add a new instrumentation for long animation frames.
And… I was looking to see, like, if anyone has… has any, Experience, like, with consuming, this data.
Because I don't know, like, if it's gonna be, like, a lot of data, like, really busy… And, like, if it should be… if it should… if it should be… if we should be collecting this data the way, it is… it is reported through… by the browser directly, and generate, like, tons… tons of events, or if it should be something more aggregated, or, You know, more sampled.
So… Yeah, I don't really have… a direct experience with this, with this API, and, like, how useful it is, so I was looking for feedback before we accept this.
**maxime quentin** 04:21 On this one, I think it's very useful to have, like, Like, understands that a page has a long admission frame.
Sometimes it's more valuable than having all the, like, long tasks or equivalent, events themselves.
However, if it's an… an instrumentation that you can opt-in or opt out, I mean… It goes back a bit, like, to the entity, entity question, like, could we have, aggregation over, like, a page, and then… If you have a long animation frame, you report it.
Or you do, like, some kind of, Instead of sending, like, hundreds of long admission frames, you only report it 5 times, and then you stop recording it, or you turn off the instrumentation if you Send too much traffic.
But, yeah.
There is value about knowing that your page is loading slowly, because you have long animation frames.
**Cleo Schneider** 05:37 I'm curious… I'm not super familiar with this… Api, but, what… what constitutes long here? Is that configurable?
Is that a static number?
**maxime quentin** 05:56 From what I remember, it's like, when you're having a script that is too long, or when you're taking Something is too long.
the API report a long animation frame by design.
then, I don't remember exactly what is the trigger, but, Super BlyQPA… was OPA, sorry, it's wrong.
**Chris Chestnut** 06:25 I mean, it's like…
**Cleo Schneider** 06:26 milliseconds. Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:29 Yeah.
**Chris Chestnut** 06:30 It, it, oh, sorry, is my mic working?
**Cleo Schneider** 06:32 Yeah, you're good.
**Chris Chestnut** 06:33 Okay, sweet. I didn't see the green. I mean, this reminds me of some of the stuff, we saw on the Web Vitals. Is this PR adding… Like, log animation frame to that, like, performance-based library?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:51 And if you're asking, like, is it as… is it updating the Web Vitals instrumentation?
That's right, yes. So it's a separate instrumentation. It's being added as a separate instrumentation. And essentially, like, every… like, when the observer yeah, observes, like, the, every… Every time, like, there's a… yeah, long frame, then it would generate an event. So that's the other thing, it's like, this seems to me like, potentially could be a lot of events being emitted, And I, like, I don't know, like, if you would want to have this enabled only, Like, in, in, diagnostic mode, or… Or maybe just, like, in a, in a sample, like, subset of, of, you know, like, a sample. So, like, at the very least, like.
like, I wonder, like, if we should have some kind of recommendation of how to use this instrumentation?
The other option would be, Like, adding additional configuration where you could, you know, filter out, like, or define, like, what the, what… How big of frames, like, you would be… you want to be reported, so…
**maxime quentin** 08:12 But, to my perspective, Knowing that a click, generated a long animation frame.
is more useful than having all the long animation frame events that you cannot connect to any kind of action or interaction.
But then it brings the instrumentation to another level, which is more like, It's not just to populate a signal when you have an animation frame, you need to create it.
So, yeah.
Unless we debounce it, and we make sure we never send more than 5 in a row, or something like that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:56 Yeah.
**Cleo Schneider** 08:58 Or would we want, sort of, like, a per-session count of how many times this thing happened?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:05 Yeah.
**maxime quentin** 09:06 Could be a… Per session, or per page, or…
**Cleo Schneider** 09:09 For bridge, yeah.
**maxime quentin** 09:11 Usually, I guess, if you have one… Page that is very slow, it will probably generate most of your long animation frames.
And if your session is, like, 3 hours, you don't really know which is the page that made the whole mess.
But, like, you're right, we need some kind of IR-level aggregation.
**Chris Chestnut** 09:33 Yeah. See, all this is just kind of reminding me of, like, when we looked into supporting instrumentation for Core Web Vitals, because I think there's currently, like, in the experimental folder of of the hotel browser, repo,
**maxime quentin** 09:51 Excellent.
**Chris Chestnut** 09:51 Support for slow… slow interaction events?
which I think do some, like… deduplication of, like, a session for specifically, like, the longest.
Longest animation frame?
I've got a link to the, to the Web Vitals, read me.
Yeah, you're there.
I thought,
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:18 I don't have a reader.
**Chris Chestnut** 10:18 Yeah, am I just mistaken about that?
So, to me, it seems like there's some overlap here between what this PR is proposing and what's already in the repo.
**maxime quentin** 10:28 So, I think the web vitals are, like, the, google, like, long, CLS, And then they've been, added to most of the Browser now.
But they are not really, they can be connected to a long animation frames, but it could be, like, just you have a layout Swift in your page.
It's like, how long does it take to have your page interactive and everything?
While a long animation frame could be, like, your page is loaded, you click on a button that Run a script, and then you have a longer animation frame.
Those vitals are more, like, at the loading of your page, you will have, like, No.
One vital that means that, one other that means something else.
**Chris Chestnut** 11:20 Oh, okay, thank you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:21 And I think the CLS is essentially, like, the jank, right? The metric that captures Jenk, but it's… I think it's… it doesn't report everyone, everything, like, the report's, like, the biggest one.
Within some time period, some…
**Chris Chestnut** 11:43 Gotcha. Thanks for the clarification.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:45 Yeah.
Anyway, okay, yeah, I'll see if, I'll see if… and then maybe I'll ask this, in the Slack channel as well, and see, But if you have, yeah, if you have any more thoughts, please add it on the PR.
I think at the very least, I mean, we could probably accept this… Since it's experimental, but at the very least have some kind of description of what to expect.
**maxime quentin** 12:16 I'll have a look and, give some feedback about it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:24 Okay, and Jared has a request on this one.
Yeah, this PR has been open for a long time, and I think… It's… important, so… yeah, if you can… I think we need more eyes on this.
So please take a look. And it's essentially, like, currently our instrumentations are… Used the base class from the JS… Instrumentation package… Let me see… Maybe this is… so this is changing it to have our own instrumentation-based class, I think.
Hmm.
Here.
So, yeah.
If you have time, please take a look at this. I think this would be good to have this, have this reviewed.
Yeah, that's pretty much it. Any questions on this?
Does anyone have anything else to talk about?
By the way, just, just for your information, like this, I think I shared this last time.
But… For anyone who doesn't go to the… Client SIG… This, semantic conventions client-side repo is getting bootstrapped.
Still very early, there's nothing there quite yet, but, I think the goal is to have our… Our semantic conventions be captured here in this repo?
So I had, you know, I had some issues and a PR open in our SDK repo to add semantic conventions there, but I think it's instead going to move here.
So that's just a FYI.
**maxime quentin** 14:49 Do you think it could, like, open the question of resource timing, semantic again, in this client-side SIG, or are we okay about having several semantic for different platforms?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 15:06 Are you referring to the, to the, like, the effort for unified HTTP.
Yeah. Yeah, okay.
**maxime quentin** 15:14 Or it was, like, either we go… we have our own Browser semantic from ZPI, and they are their own, but then we didn't know if we wanted to have something for everyone, or…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 15:26 Yeah, I mean, I think… I think what I would like to do as a first step is, like, to just, Put the conventions that we have in our instrumentations currently here.
And then… Yeah, if you want to revisit that topic, we can.
Yeah.
That's risk.
I mean, I think I'm open… To, to looking for, like, unified, semantic conventions for that, for that, but, I haven't actually had time… I haven't had time to, like, be driving that, so… No.
Alright, anything else?
**maxime quentin** 16:14 No, no, good for me.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:18 Alright, sounds good, we can, we can just have a short meeting then.
Thanks, Mark. Thanks. Thanks, everyone. See you.
**maxime quentin** 16:26 Come on.
**Cleo Schneider** 16:27 Thanks, yo.
