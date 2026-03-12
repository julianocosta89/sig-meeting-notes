SIG: Developer Experience SIG Meeting
Date: 2025-07-02
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:20 Hello! There!
**tristan** 00:26 Hey! Good morning!
Boom!
**Juliano Costa | Datadog** 00:30 What's up?
**tristan** 00:41 Anybody else, join.
**Juliano Costa | Datadog** 00:47 Just checking the the chat messages.
**Damien Mathieu** 00:51 Hey! Good morning!
**tristan** 00:53 Hey! Hey!
**Juliano Costa | Datadog** 00:54 Good morning.
Were you in in Denver then? I mean, you mentioned a conference last week.
**Damien Mathieu** 01:06 No, it's no I was it's called Sunitech. It was in Montpellier.
**Juliano Costa | Datadog** 01:16 Cool, cool.
**tristan** 01:25 We can't believe they had that Denver Conference right after I was there.
**Juliano Costa | Datadog** 01:37 Everything happens when when we leave the places.
**tristan** 01:40 Yeah.
and we could probably get started. Maybe Steve will join.
That'd be good. Yeah. One second so regarding the collector blog posts.
Have you guys done an interview, or set up a time for interview with Mastodon?
My.
**Juliano Costa | Datadog** 02:20 I reach out to Hano. He told me to reach out to team. Who is the responsible for for deploying and managing the collector.
but he said that he may take a while to reply, because, they are busy. Well, that's the thing with mastodon. They are a small team managing everything, so I don't know how long it will take. But on the mail I already explained and shared the outline that we kind of have and ask him to just give me like 1 h, and we can maybe go over. I record the session, and then I I build the the whole thing. And so what I would need from what I said that I would need from from him is kind of joining this call, discussing and then reviewing the the blog whenever he's ready.
so it should be lower for it, so to say. But yeah, I need to. We need to get them brist good.
**tristan** 03:30 So I've been talking with the and use the mixture end user group as well as Atlassian and a company. The end user group put me in contact with skyscanner.
They're in travel company, like booking flights and stuff.
I got mixed up because I was talking to 2 people in the end user group. And I thought they were both talking about the same company when I was discussing with them.
So it turns out, there's 2 potential companies. There's skyscanner and one other. I still don't know the name of and Skyscanner is pretty well. No, the other company. So yeah, I got mixed up here, too, because I thought Sky scanner was the large one.
but I've already so skyscanner and Atlassian I've already talked to about what we're we'll need.
And that will do just a an interview, and that they're down for that. I just gotta schedule the time. I hope to do that within.
Probably, I guess next week I guess I'm supposed to kinda off Friday again.
And the so the question is, gonna be for this group is what to do, that we have 4 companies and when I was thinking so, the company that no, I know this guy's wait one second. I'm getting all mixed up.
Okay, skyscanner is of 500 to a thousand engineer range company So a lot of engineers they have a multiple clusters running that. Then send to a gateway deployment. So and they're they're running demon sets as well, of course, and they have a thousand plus services. So this started to sound to me like quite a jump from mastodon. So we might want to do, since we also have Atlassian.
We have Alassian skyscanner mastodon, and we have this other company that I still don't know the numbers on, or even the name of. That. Hopefully, I'll find out very soon, even, maybe during during this call maybe they'll fit in there between Macedon and Skyscanner, and we could do 4 small medium, large, extra large.
**Juliano Costa | Datadog** 06:44 Yeah, we're we're missing the the media one. Right?
**tristan** 06:47 Yeah, yeah, that the from the end user group medium would be smaller. So I'm hoping the other one's gonna be the other option. Besides, skyscanner is gonna be smaller. But I think Skyscanner would be a good company to talk with, so I don't wanna drop them for being too big, because they are.
An Atlassian, hey?
And that'll drop it lasting too large.
**Juliano Costa | Datadog** 07:16 Yeah, I think sky scanner is also a good story because they are.
I think they're pretty mature on hotel, because Dan Blanco was there.
**tristan** 07:27 They've been on so probably.
**Juliano Costa | Datadog** 07:31 He's been talking about hotel for for a long time. So yeah.
**tristan** 07:36 Yeah. He's who connected me with them.
**Juliano Costa | Datadog** 07:40 Good.
**tristan** 07:43 So yeah, once we find out who this other company is.
Hopefully, they fit in there into a medium size. And they're like, you know.
one decent size deployment or something, and some demon sets and not multiple clusters sending to a cluster and a thousand engineers or something. Hopefully, they're you know, in the 100 engineers range 100 services or something there, there's probably some companies I could reach out to.
**Juliano Costa | Datadog** 08:26 It's weird, because we always hear about the the big cases. The big companies.
**tristan** 08:31 Right.
**Juliano Costa | Datadog** 08:32 Yes, and hmm.
**tristan** 08:35 Cool.
Oh, wait! Oh, maybe you might have Grock GROQ
**Juliano Costa | Datadog** 08:51 You?
Okay, what's it? EROQ.
**tristan** 08:55 Yeah, there's some AI company.
**Juliano Costa | Datadog** 08:58 Okay.
**tristan** 09:01 I have a friend there, and I noticed recently they're hiring for an open telemetry person and so they might. I don't know if they're already moved over or not. But I think they're in the medium size range we're looking for. So if they are, yeah, I'm gonna reach out to my friend and find out in case this other company the end user group has is like a thousand engineers and all that.
Okay, I'm gonna Ping Shawn when he gets up.
But yeah, hopefully, I'll hear soon, also who this other company is.
and they might be using the airline SDK. So that'd be nice.
**Juliano Costa | Datadog** 10:02 They have this the positions to open staff observability engineer.
**tristan** 10:07 Yeah.
could mean that they alright.
**Juliano Costa | Datadog** 10:13 They haven't started yet.
**tristan** 10:15 Right.
**Juliano Costa | Datadog** 10:16 Awesome.
**tristan** 10:17 We'll see.
Okay.
yeah. What else there is there anything else we need to discuss there with the the interview? Anything you guys wanted to discuss before you go just kidding.
**Juliano Costa | Datadog** 10:51 Maybe one thing to to Damien. If if you could take a look at the the outline that Tristan and I came up with, and see if you.
if you have any suggestions or anything.
**Damien Mathieu** 11:04 Sorry I missed it. Where is is it in slack in.
**Juliano Costa | Datadog** 11:09 Oh!
**tristan** 11:10 So it's a tab in the Sig Google, Doc.
**Damien Mathieu** 11:16 Okay.
**Juliano Costa | Datadog** 11:18 Let me share with you.
**tristan** 11:20 Can I link directly to it? Oh, you got it. Okay.
perfectly.
**Damien Mathieu** 11:33 I'm I'm on it.
**Juliano Costa | Datadog** 11:35 Okay, cool. Yeah. No need to to stay in the call to to
**Damien Mathieu** 11:41 I.
**Juliano Costa | Datadog** 11:42 So we can. We can do this. Async, yeah.
cool. And if anyone comes up come comes across any medium sized company that gives us.
**tristan** 11:54 Do you have.
**Juliano Costa | Datadog** 11:55 Raise your hand.
**tristan** 11:57 Yes, cool.
I'll let you guys know if I soon find out who this other company is. So and if we have a medium company handle. But yeah, until then. Yeah, keep in mind and maybe poke around.
**Juliano Costa | Datadog** 12:11 Awesome.
**tristan** 12:12 Alright!
**Juliano Costa | Datadog** 12:13 Cool, then have a good one.
**Damien Mathieu** 12:15 Likewise talk to you later.
**tristan** 12:17 Yeah, later.
