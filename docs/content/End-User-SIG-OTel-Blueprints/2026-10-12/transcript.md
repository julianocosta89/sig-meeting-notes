SIG: End-User SIG: OTel Blueprints
Date: 2026-10-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Lukasz Ciukaj (Splunk Inc.)** 09:03 Hey Dan.
Good afternoon.
**Dan Gomez Blanco (New Relic, Inc.)** 09:09 Hello.
**Lukasz Ciukaj (Splunk Inc.)** 09:11 Sorry for being late.
**Dan Gomez Blanco (New Relic, Inc.)** 09:13 That's okay.
**Lukasz Ciukaj (Splunk Inc.)** 09:15 Took me a while to come back home and get some emergency stuff, so… That's the reason I'm 10 minutes late.
**Dan Gomez Blanco (New Relic, Inc.)** 09:22 All right.
**Lukasz Ciukaj (Splunk Inc.)** 09:22 Nobody else here apart from you?
**Dan Gomez Blanco (New Relic, Inc.)** 09:26 Say that again.
**Lukasz Ciukaj (Splunk Inc.)** 09:27 Nobody here apart from you?
**Dan Gomez Blanco (New Relic, Inc.)** 09:28 No, nobody joined yet, so, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 09:34 Okie doke.
So.
**Dan Gomez Blanco (New Relic, Inc.)** 09:38 But yeah, hopefully everything's all right. Yeah.
**Lukasz Ciukaj (Splunk Inc.)** 09:40 No, no, no, nothing, nothing super urgent, like, I had to, you know, move some meetings around, and that's the reason I canceled the other one, and here I'm late, and also… but no, nothing, nothing serious. It's okay.
**Dan Gomez Blanco (New Relic, Inc.)** 09:51 Cool, cool, cool.
Okay, so there's maybe a quick one, actually. Yeah, no. Yeah.
**Lukasz Ciukaj (Splunk Inc.)** 10:02 we are with Blueprints. I've seen that Alex is still working on his one.
**Dan Gomez Blanco (New Relic, Inc.)** 10:08 Yeah, I reached out to Alex, last week. I think he's, yeah, he's had… Not much bandwidth, but, like, yeah, he was gonna get that sorted, or the… the review, comments. To be fair, it's almost ready to go. Tiffany reviewed it for copy edit.
I think it was just, I think, you know, the diagram that was used.
was a bit of, like, a Claude-generated diagram, and I just.
Gave an example of, like, I almost use. I use Claude to reverse.
reverse engineer the quad PNG into like a mermaid diagram that represents the same thing, I think.
**Lukasz Ciukaj (Splunk Inc.)** 10:53 HBMI.
**Dan Gomez Blanco (New Relic, Inc.)** 10:54 of updating that.
**Lukasz Ciukaj (Splunk Inc.)** 10:56 Yeah, and I see Patrice did some, also… some changes, and he approved that. But then, my comment about changing the title, I say, it seems it got ignored, so nobody picked this up, and I don't know if Alex is about to change the title of this, or it will stay as it is. I don't know.
**Dan Gomez Blanco (New Relic, Inc.)** 11:18 I.
I mean, we can always… Let's see, I don't know, let's see if… let's speak to Alex and see that… make sure that he gets that. If you can send him a message, maybe that would help as well?
**Lukasz Ciukaj (Splunk Inc.)** 11:30 Yeah, I will, I will, I will send a message and tag him in the…
**Dan Gomez Blanco (New Relic, Inc.)** 11:33 Do we say, do we say, maybe we can add it here so it doesn't get ignored?
**Lukasz Ciukaj (Splunk Inc.)** 11:39 Yeah… I… suggested, I mean, ChatGPT suggested some stuff for me, like observability architecture for Kubernetes environments, observability patterns for Kubernetes environments.
Telemetry architecture, building observability in Kubernetes environments, open telemetry deployment in Kubernetes. So this is, like, more… Details.
**Dan Gomez Blanco (New Relic, Inc.)** 12:02 Well, if you do, because I think, you know, I want to change the name of the blueprint that I wrote.
And.
Because the word workload, I don't think…
**Lukasz Ciukaj (Splunk Inc.)** 12:12 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 12:12 It really represents that well. However, I think, you know, if we think about.
Kubernetes cluster observability, that could be.
I think that could be a better name personally, because.
**Lukasz Ciukaj (Splunk Inc.)** 12:24 For for you for your, blueprint. Right?
**Dan Gomez Blanco (New Relic, Inc.)** 12:27 No, no, for this one.
**Lukasz Ciukaj (Splunk Inc.)** 12:28 For this one.
**Dan Gomez Blanco (New Relic, Inc.)** 12:29 Because this is, we're only talking about cluster observability, really, not about.
Or even, like, maybe we can say Kubernetes infrastructure observability.
**Lukasz Ciukaj (Splunk Inc.)** 12:40 infrastructure…
**Dan Gomez Blanco (New Relic, Inc.)** 12:41 Maybe like Karna is going into.
It's more like… I don't know.
I think Kubernetes cluster is probably okay.
What do you think?
**Lukasz Ciukaj (Splunk Inc.)** 12:51 It could be like observability patterns for Kubernetes.
**Dan Gomez Blanco (New Relic, Inc.)** 12:55 Mmm.
**Lukasz Ciukaj (Splunk Inc.)** 12:56 Elementary architecture or building observability for Kubernetes cluster. So something like that.
**Dan Gomez Blanco (New Relic, Inc.)** 13:02 I mean, when we do other Blueprints, we said, for example, managed telemetry platforms, or we said…
**Lukasz Ciukaj (Splunk Inc.)** 13:09 you know.
**Dan Gomez Blanco (New Relic, Inc.)** 13:09 QMIT or process and infrastructure monitoring, right? So the Blueprint itself tells you, the title tells you what we're, you know, the environment pretty much and the scope in a way.
And I think if we think about this is like what we're really the scope of this is the cluster, right? It doesn't extend anything out into anything else.
Well, it does, a little bit, but it's control plane, like, observability.
Apart from the cluster, so… For the cluster itself. So I'm not sure if we just say, I don't know. Because Kubernetes observability, I agree, that is too wide.
And.
**Lukasz Ciukaj (Splunk Inc.)** 13:56 It's… maybe Alex has some ideas. It's his…
**Dan Gomez Blanco (New Relic, Inc.)** 14:00 Yeah, that's it.
So let's explain that, what we're saying now here, And I'll tag you as well.
**Lukasz Ciukaj (Splunk Inc.)** 14:11 So you're adding that to the notes?
Of the meeting, or what?
**Dan Gomez Blanco (New Relic, Inc.)** 14:15 Am I sharing my screen, or…
**Lukasz Ciukaj (Splunk Inc.)** 14:17 No, you're not.
**Dan Gomez Blanco (New Relic, Inc.)** 14:19 Really.
**Lukasz Ciukaj (Splunk Inc.)** 14:20 Oh, no. You're sharing. Sorry.
**Dan Gomez Blanco (New Relic, Inc.)** 14:21 All right.
**Lukasz Ciukaj (Splunk Inc.)** 14:22 I'm not totally with you.
**Dan Gomez Blanco (New Relic, Inc.)** 14:23 I thought I wasn't. Yeah, so I say, let's say name this something else. The current name is a bit too wide. We're thinking… Something that.
Describes the context, the… sorry, the environment…
**Lukasz Ciukaj (Splunk Inc.)** 14:40 or the content maybe of the Blue Book.
**Dan Gomez Blanco (New Relic, Inc.)** 14:43 Yeah.
for example, Kubernetes Cloud Service for Ability.
**Lukasz Ciukaj (Splunk Inc.)** 14:53 That is a little bit better, yep.
**Dan Gomez Blanco (New Relic, Inc.)** 14:59 Right, okay, cool, let's do that.
Yeah, if you can send Alex a message, I think the only other comment is, here would be… and I think this is fine for me, I think I'm gonna resolve it. Can I resolve it? No, I cannot resolve it.
Because, yeah, so Tiffany said.
Well, this says, use the open telemetry operator as a collector control plane, and scrape Prometheus targets node locally.
That sounds okay to me, because we're talking about no local… Prometheus scraping.
Node locally.
Sounds odd.
I mean… I don't, I can't think of any other word to explain what we're trying to.
To say.
**Lukasz Ciukaj (Splunk Inc.)** 15:43 Yeah, no, okay.
It's don't look any. So yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 15:49 Yeah, I'll just say, can I resolve a comment?
Alex, can you resolve?
If you agree.
Yeah, so then I caught something here which it says use this decision tree used to have that.
That graph for the decision.
**Lukasz Ciukaj (Splunk Inc.)** 16:15 Hmm.
**Dan Gomez Blanco (New Relic, Inc.)** 16:17 But that's… there's not any more in there, so I just caught that.
And then, what is… what's that here? We use a diagram below. Alright, so… It's just a change of word in there.
And we use the diagram below. So the diagram is, instead of being… where is the image? Instead of being this one, right, which is the current diagram.
Do you know there's one thing that Claude does a lot of times, which is like adds a lot of words into.
**Lukasz Ciukaj (Splunk Inc.)** 16:47 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 16:48 Yeah.
**Lukasz Ciukaj (Splunk Inc.)** 16:49 When you see that, you immediately know this is AI-generated stuff, and yeah, I agree.
**Dan Gomez Blanco (New Relic, Inc.)** 16:54 So, I added this one, which… Yeah, basically.
It follows that style. I mean, again, you know, we can change the style, I don't care, but it's… Is, it should basically follow that.
**Lukasz Ciukaj (Splunk Inc.)** 17:09 It looks much better to me. I'm… yeah. If I would have to choose, I would choose this one.
**Dan Gomez Blanco (New Relic, Inc.)** 17:18 Right, so that's it, and for the rest, I think it's all…
**Lukasz Ciukaj (Splunk Inc.)** 17:23 Cool.
Hmm, yeah.
So this one, and did you get any feedback from you know the DevEx team? You remember we spoke last time. Did you ping them or not?
**Dan Gomez Blanco (New Relic, Inc.)** 17:33 I did not. However, I was chatting to Johanna about something else, and I asked about that.
**Lukasz Ciukaj (Splunk Inc.)** 17:39 Can we put it as an item? Because I believe the last time, we were thinking about adding it on the… Or is it already an item here?
**Dan Gomez Blanco (New Relic, Inc.)** 17:50 Yeah, it's this one.
**Lukasz Ciukaj (Splunk Inc.)** 17:51 Oh, this one, okay.
**Dan Gomez Blanco (New Relic, Inc.)** 17:52 Yeah, just put it in progress. I'll give a… I'll give an update and give them… Yeah, it's basically reference implementation.
**Lukasz Ciukaj (Splunk Inc.)** 17:57 Yeah, the priority here, or something, you know, so we don't forget about this. Can we change here, or…
**Dan Gomez Blanco (New Relic, Inc.)** 18:03 I'll put it on hold, because it is on hold at the moment, and then that should flag to us that is…
**Lukasz Ciukaj (Splunk Inc.)** 18:10 Right.
And isn't the same, like, agree on missing reference architectures to complement Blueprints?
**Dan Gomez Blanco (New Relic, Inc.)** 18:15 I think we can close… I mean, yeah, I didn't… So the last comment was, like.
**Lukasz Ciukaj (Splunk Inc.)** 18:23 Not nice at all, yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 18:25 This is more like, I don't think we need to… to be able to close a project. If we have the five reference implementations, I don't think to close the… sorry, to close the bootstrap of this.
**Lukasz Ciukaj (Splunk Inc.)** 18:37 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 18:37 We need to, we need to have this done, but it would be good to… as part of this, basically agree on, like, what type of reference implementation will we be looking for. It's just so we can call it out in the, in the, in the… in a blog post when we wrap up the project, right, and say, hey, you know, by the way, it would be great if you have this type… we created this blueprint for infrastructure monitoring. If you're using OPAMP, or if you're using, you know, OTel and infrastructure, it would be good to have your reference implementation. That would be… that would be a good call-out to the community.
But yeah, so if you, if you can drop a comment here, if you have some time on like, you know, so I think the, the one that I wrote is pretty much covered.
Everything that we talked about there.
covered by the ones that are currently there, like Adobe Mastodon.
**Lukasz Ciukaj (Splunk Inc.)** 19:29 sky's.
**Dan Gomez Blanco (New Relic, Inc.)** 19:29 under the cover things.
The one that… Leo.
**Lukasz Ciukaj (Splunk Inc.)** 19:35 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 19:36 Observability is the cluster observability, I don't think is.
Too well covered.
Yeah, so I think it's mostly around the area, the, you know, the blueprint that you wrote about the infrastructure. If we can get something, some reference implementation that tackles that, that would be great, but I don't know, maybe if you write here what sort of things.
**Lukasz Ciukaj (Splunk Inc.)** 20:01 Maybe, but I'm thinking now, maybe we could drop a message in End-User… but no, but that would require… Writing a new reference implementation, right, and we cannot make it by, let's say.
in the next two weeks to have this project closed. I mean… Yeah, I think…
**Dan Gomez Blanco (New Relic, Inc.)** 20:19 I think it's… I don't think we need it. I think, you know, to be fair, like, Yeah, I don't know…
**Lukasz Ciukaj (Splunk Inc.)** 20:27 I will respond to this to this to your last comment that that I don't I mean I have one customer in mind that I know they are doing something like that but it's they will be not happy to to to go public so I know that.
But what we could do at some point, maybe drop a message in End-User Slack channel, asking if there are any customers that are, like, implemented, something similar, that would be happy to… to publish the reference implementation, so then we could link that to this blueprint. So so that is something so so I will put post a comment like that, so we close the this this issue. And but again, I agree with you that it's fine to just publish blueprint, we don't need to have like any reference implementation linked to it. It's it's not mandatory, right? It would be nice to have the real implementation, but if we don't have yet, that's fine.
Yeah, let's keep going.
**Dan Gomez Blanco (New Relic, Inc.)** 21:17 Yeah, one thing… Yeah, I just thinking like Nike.
I think in the… in America, you pronounce it Nike, I think.
**Lukasz Ciukaj (Splunk Inc.)** 21:27 Maybe.
**Dan Gomez Blanco (New Relic, Inc.)** 21:28 But I did a presentation at KubeCon.
Atlanta, where they, they talked about OPAMP and how they use it.
Okay. Maybe I could reach out to them.
**Lukasz Ciukaj (Splunk Inc.)** 21:41 Do you have any contacts there or not?
**Dan Gomez Blanco (New Relic, Inc.)** 21:43 I had a brief chat with one of them that presented that. Apart from that, like, not sure if that qualifies as a contact, but yeah, I did chat to them, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 21:54 Yeah, but that's a good idea, so maybe we can reach out Nike team, or I don't know.
Maybe… maybe they have some contributors as well to OTEL, so maybe we could identify them. Yeah. And… or there's someone who presented at KubeCon, so that's a good, good idea, so then we could… that would be the same as with Airbnb that I told you last time, that we know that they did something cool, they already presented at KubeCon, so there is, you know, this… Is that there is a strong possibility that they will be happy to write some some some reference implementation and publish that since they already spoke at at Coupon. So yeah, good idea, but I'm not sure if that is blocking at the moment, right? So so that is nice to have. We can add it later, but but don't don't treat it as a blocking item. Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 22:38 Sounds good.
All right.
Anything else? I think we've got the presentation for, or the talk at KubeCon, so that's got you and I a little bit busier on that front, but.
**Lukasz Ciukaj (Splunk Inc.)** 22:51 No, we good. No, nothing here. I think how about the blog post? So, so once we publish the Alex blueprint, we sort out the other stuff. What do you think? Should we start working on the blog post and wrapping up the.
The project?
**Dan Gomez Blanco (New Relic, Inc.)** 23:07 Yeah, I mean, if you… if you have any… If you want to take that issue on about wrapping the OTel projects, or, you know.
There is other parts that I think we can, you know, I can call it complete.
**Lukasz Ciukaj (Splunk Inc.)** 23:22 Yeah, I can start drafting something, maybe OpenPR and link that to this issue so we can start reviewing it and work towards publishing it.
**Dan Gomez Blanco (New Relic, Inc.)** 23:32 Cool. Yeah, or even, like, I don't know, if you don't want to open up PR, just, Google.
**Lukasz Ciukaj (Splunk Inc.)** 23:37 Oh, Google Doc, yeah, yeah, something like that. Yeah, I think that's… that would be… Yeah, that's something that we need anyway for our presentation, so we can use the same contents and same knowledge, or same, you know, the bandwidth for working on the… because it would be great to have it published before the KubeCon. Do we need to publish it before a KubeCon? What do you think?
**Dan Gomez Blanco (New Relic, Inc.)** 24:00 We have a month, so I think we can, aim to.
**Lukasz Ciukaj (Splunk Inc.)** 24:04 Per month, I think it's a little bit less. Oh, no, it's a month.
**Dan Gomez Blanco (New Relic, Inc.)** 24:07 Okay. Well, I mean, it's a month, because we are…
**Lukasz Ciukaj (Splunk Inc.)** 24:10 just.
**Dan Gomez Blanco (New Relic, Inc.)** 24:10 Is 9 to the 12th.
**Lukasz Ciukaj (Splunk Inc.)** 24:12 No, but I think that, you know, if we go there on the stage and saying, oh, this is something that is already done, completed, it sounds better than all, we are still in the bootstrap process, so let's try to close this, like, I will try to find some bandwidth for working on this blog post.
And also, maybe some video promo, or whatever, so then…
**Dan Gomez Blanco (New Relic, Inc.)** 24:35 Let's start with that. The moment that, you know. Yeah, we can definitely. This is a blog post that's coming from is different from an end user blog post. So it should, you know, and we've got Tiffany there as well that can help us with that. So yeah. To review it in the, in the website. So yeah.
**Lukasz Ciukaj (Splunk Inc.)** 24:51 It shouldn't be long, I think we should summarize what was done, what was published, what we agreed on, kind of the same as we have for presentations. So, yeah, let's try to do it. I will try to find some bandwidth, and let's prioritize it. So, I prefer to have this part closed.
And we can continue working on this.
**Dan Gomez Blanco (New Relic, Inc.)** 25:11 Awesome.
**Lukasz Ciukaj (Splunk Inc.)** 25:12 Cool.
**Dan Gomez Blanco (New Relic, Inc.)** 25:13 Alright, I think that's it.
**Lukasz Ciukaj (Splunk Inc.)** 25:15 That's it for today. Thank you, Nathan, for today, and talk to you tomorrow morning.
**Dan Gomez Blanco (New Relic, Inc.)** 25:18 Yeah, right, see you, bye-bye.
