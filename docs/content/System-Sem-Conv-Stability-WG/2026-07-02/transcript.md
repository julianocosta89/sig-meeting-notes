SIG: System Sem Conv Stability WG
Date: 2026-07-02
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:01 Hello.
**Dmitrii Anoshin** 02:47 Oops.
**Pablo Baeyens** 02:49 Blue.
I think that's probably everyone, because… Write on his own.
Yeah, I guess I… One topic put on the agenda, just… I mean, so Brainer left a comment on the issue I filed about, system file, system attributes.
It seems to me like… at least type, mountPoint, and mode are… Good to go, other than, like, maybe… Tweaking the descriptions a bit.
Braden says, I think this name sucks for, system file system state, I don't know if anybody has a… A different suggestion for a name?
That would be the… What are the… State is free, preserved, or used.
Honestly, I'm not very good with coming up with names for this, but… If nobody has suggestions, we can wait for Brandon and see if he has an actual… Alternative to suggest.
**Dmitrii Anoshin** 04:32 Yeah, I guess that's the way to go. I don't have a strong opinion, I'm not… The one who would fight for names.
So…
**Pablo Baeyens** 04:42 Nope.
Okay, let's…
**Dmitrii Anoshin** 04:45 What about the ballpark?
**Pablo Baeyens** 04:46 Wait, then…
**Dmitrii Anoshin** 04:47 Okay. And to be honest…
**Pablo Baeyens** 04:49 Yeah, and I mean, if you haven't taken a look at the issue.
and you have a different opinion, I guess leave a comment.
I… I think it's better if I open a PR just for all of them.
Instead of… Twin the one side.
That we are all, like, ready.
So I'll wait until next week.
What are we going to be like.
**Christos Markou** 05:21 Are those used, I assume they're not used outside of system, area, right? They're not shared, or anything like that.
**Pablo Baeyens** 05:30 No, I don't think so, no. They are used on system file system metrics.
And that's it.
**Christos Markou** 05:42 There was a shared… FS type, or something like this?
Yeah, never mind, I can look for it, and… Verify.
If we have anything that is relevant to this that we should take into account.
**Pablo Baeyens** 06:00 Okay.
Yeah, I mean, Just as proof of what I said, if you look at that GitHub search.
I think the only… Places this is mentioned are all, like, either system metrics or the registry.
So, you know, doesn't seem to be used anywhere else.
Okay, yeah, I guess we can go to… Dimitri's topic.
**Dmitrii Anoshin** 06:45 Yeah, it's the same topic from the last week. I just wanna raise… awareness about this PR. Christus has suggested using a feature gate. I'm okay with that, however, it's already kind of one.
Option on the configuration to toggle that.
So, adding FisherGate on top of that.
Kind of makes it… maybe… not that useful.
as for other use cases where we typically use Fisher gates. So.
Hey, I want to hear your feedback.
And… Potentially, see if we can… I'm pretty sure you bring in the air system.
**Christos Markou** 07:43 I was only concerned… my only concern was that, might be… like… Badly breaking for some use cases.
We checked with Roger, we chatted a little bit about this. In our case, it seems it should be fine.
Since aggregations should continue working, no matter if the attribute is there or not. But I wonder if maybe someone outside… out there already relies on this attribute specifically.
**Dmitrii Anoshin** 08:17 You see it.
Ask us.
**Christos Markou** 08:20 Maybe… we do breaking changes all the time and contribute, so that might not be a big deal.
So, probably I would be fine, but, yeah.
**Dmitrii Anoshin** 08:31 Good, Sharon.
**Christos Markou** 08:32 I'm not… if everyone else agrees.
**Dmitrii Anoshin** 08:35 The first.
**Christos Markou** 08:35 doing it directly, I would also be fine.
**Dmitrii Anoshin** 08:38 I really decided…
**Christos Markou** 08:39 Just share the concern.
**Dmitrii Anoshin** 08:40 Let me bring something, some, like.
inputs from my experience so far, what I see people use.
Like, I, First of all, to be clear, we do aggregate that on Splunk observability side, over CPU. Also, do I see… I saw a lot of users who aggregate that on the collector as well.
So my impression is that the vast majority of people don't care about CPU time over core, and they aggregate. Well, maybe vast majority, but majority, I would say. So, for the majority, it'll be… positive change, it'll be not breaking, and it'll reduce cost of, Data storage and transferring.
for… smaller portion, portion, not sure, I cannot quantify. For them, it all will be break and change.
But if we put, like, pretty good, change lock item, I guess it should be fine, because it's just one, like, configuration option to bring it back. Super nice.
**Roger Coll** 09:58 Yeah, for me, I don't have a strong opinion either. I think it's fine to just go ahead. We have done a lot of breaking changes similar to that, also semantically. But another option that I was thinking is maybe land it in the semantic conventions V1 feature gate, that we want to introduce for the… Host metrics, and put all the stuff for… B1 there, let's say the… And this would be together with the, let's say, the rename of the CPU attribute as well, that it will be… CPU logical.logical number.
Because let's say that we made this change in the semantic conventions, I think, a few months ago.
So if we want to introduce a feature gate, I'm not sure about this.
Maybe we can reuse that one.
So, starting adding it, it's another option, just to… Dimension.
**Dmitrii Anoshin** 11:04 We can break it down by the ex… by… by the user experience, right? Let's say those who aggregate now. We are… we are removing one attribute to worry about.
Before we… we change.
Before we change the attributes, right? So, there are different… different, I don't know, aggregation languages.
But I believe in ProvQL, you can say without attribute, right?
When you aggregate, you don't say… Keep this attribute, but you can also say, Remove this attribute, right?
So, for people that are doing that, like, without… A promQuery?
It'll be… it'll be better for them, because they already can remove that re-aggregation, and when we change the attribute name going forward, they will not do anything.
But if we… If we keep it to that point.
So they will need to… Actually, they will… it'll be the same. Without… if they can keep without it, it'll be… But the next one will be opt-in. So, yeah, pretty much, I guess, there is no downside.
of Kubernet.
After… Excuse me.
But, yeah.
**Roger Coll** 12:50 Yeah…
**Dmitrii Anoshin** 12:50 I mean… It just… another thing is that we are, like, how we define what is gonna change? If we… Do not include opt-in promotion?
You know, it's cleaner… it's cleaner names only. Yeah. And, like, easier to document, it's easier to draw the line.
If we include opt-in change into that, it'll be more for users, too.
What?
**Roger Coll** 13:27 Yeah.
**Dmitrii Anoshin** 13:28 It's like a…
**Roger Coll** 13:28 Well, I guess we need to include everything, right?
Oh, you mean that all…
**Dmitrii Anoshin** 13:33 All the opportunities.
**Roger Coll** 13:35 It would be made on the main branch.
**Dmitrii Anoshin** 13:37 I'm not…
**Roger Coll** 13:38 the main.
**Dmitrii Anoshin** 13:39 You think there will be more opt-ins after that? I'm not aware of anything else.
**Roger Coll** 13:47 I don't know if we change, fuel for the process.
**Dmitrii Anoshin** 13:51 Discovery Site collection of mine.
**Roger Coll** 13:52 attributes and this kind of things, and the sterilization, I don't remember, but…
**Dmitrii Anoshin** 13:56 Might be.
**Roger Coll** 14:00 Mmm.
**Dmitrii Anoshin** 14:03 That they'll find out their unit for free time? No.
**Roger Coll** 14:05 But, yeah, I don't remember.
missing now on top of my…
**Dmitrii Anoshin** 14:09 I'm also eager to try the new capability, like, we don't have any opt-in.
**Roger Coll** 14:15 Yeah.
**Dmitrii Anoshin** 14:16 attributes at this point. So I'd like to introduce something, so users see that it's available, and maybe they can promote, or, like, they introduce new metric, they can make something opt-in. But if we don't have anything, we just have the framework.
For the user, it's, like, for component developers as well.
It's not something that… Dave. Anyway…
**Roger Coll** 14:44 Yeah, that sounds good to me. For us, basically, we just don't care about this attribute, so… Elastic basically aggregates over all of that, so it's a…
**Dmitrii Anoshin** 14:55 territory.
**Roger Coll** 14:56 It's better for us in the sense that we will have less.
**Dmitrii Anoshin** 14:58 Absolutely.
**Roger Coll** 14:59 let's say, telemetry, it will be automatically aggregated, so let's work to… so for us, it's a no change. It's good in that sense. I was just wondering, on the collectors that you were mentioning, that they do the aggregation in the edge with, I guess, processors, maybe?
**Dmitrii Anoshin** 15:18 Yes.
**Roger Coll** 15:19 Do they… will this be breaking, or we'll just continue to…
**Dmitrii Anoshin** 15:24 Like, any aggregation. That was metrics, transform, processor.
And, mattress from processor, if… if it doesn't see that attribute, it should be fine. I can double-check that, I can double check, that's a good… that's a good point. Let me… let me double check.
But that's correct.
**Roger Coll** 15:43 Yeah, then some… I mean, the reason to start trying it out before the…
**Dmitrii Anoshin** 15:48 That's an intuitive one.
**Roger Coll** 15:49 B1, Future Gate, etc.
**Dmitrii Anoshin** 15:52 Who's there, please?
**Roger Coll** 15:52 with plans.
**Dmitrii Anoshin** 16:06 Pablo, what about Datadoc? Do you rely on this attribute, or do you also aggregate?
**Pablo Baeyens** 16:13 I would bet we aggregate. I'm going to ask, but yeah, I don't… Remember right now that we… Huh.
**Dmitrii Anoshin** 16:25 Yeah, this is my pillow.
**Pablo Baeyens** 16:26 anything.
**Dmitrii Anoshin** 16:27 Yeah.
**Pablo Baeyens** 16:28 Paracore.
**Dmitrii Anoshin** 16:29 That was… yeah, that was…
**Pablo Baeyens** 16:35 I guess, let me… ask, and… Trying to get back to you.
Today or tomorrow,
**Dmitrii Anoshin** 16:48 I was on it first, and they wanted to get things in.
**Pablo Baeyens** 16:50 And other people have had time to… to look at it. You shared it on… on the Slack channel, Sam.
**Dmitrii Anoshin** 16:55 We're going against DC.
**Pablo Baeyens** 16:56 I find that convincing, that, like, most people are going to be aggregating buy it.
**Dmitrii Anoshin** 17:01 That's beautiful.
Secure the script, that one. And, she wanted to…
**Pablo Baeyens** 17:07 It's been tricky for us, because, like.
**Dmitrii Anoshin** 17:09 to the back.
**Pablo Baeyens** 17:09 those metrics are rewritten into the data log names, so I need to look at the equivalence of them.
**Dmitrii Anoshin** 17:17 Yeah.
**Pablo Baeyens** 17:18 the dashboard.
But I should be able to have an answer soon.
**Dmitrii Anoshin** 17:27 Thank you.
Order Business College.
Bye.
Yeah, literally, like, Gartner said it don't, and, like, part of it's, like, them best managing their business, because they need to have, internet balance controls, and so they did SIA and SPA.
The 60,000 employees, vice president.
You're gonna keep it touching nothing.
**Pablo Baeyens** 17:50 Okay, any… Other topics?
**Dmitrii Anoshin** 17:52 And we told him to talk, and I don't… Anyway, he told the…
**Christos Markou** 17:56 I…
**Dmitrii Anoshin** 17:57 I know.
**Christos Markou** 17:57 I know Donald is planning to work at some point, probably next week.
on, leveraging the feature gate, mechanism in M.Gen.
Probably he will pick up a single scraper from host metric receiver, and probably the process one, or since we have the release candidate already for process, and we'll try to, put this into action, so… Hopefully we'll have something to… Discuss or review next week, in this regard.
**Pablo Baeyens** 18:32 Cool.
**Dmitrii Anoshin** 18:34 ZOP…
**Pablo Baeyens** 18:36 Yeah, and the thing I mentioned about the Zoom link, I… maybe next week, or the following, we can try it out, because we need to figure out how to upload the recordings. We tried it out on the governance committee meeting, and it seems to work fine, it's just there's an additional, like, logging layer before you actually get to the Zoom meeting.
But you can, like, join as guest on… It's… should be…
**Roger Coll** 19:08 Nope.
**Pablo Baeyens** 19:09 the same.
**Roger Coll** 19:09 log in with the Linux Foundation, or… What?
**Pablo Baeyens** 19:13 Yeah, yeah, so, like… There's an ability to restrict which people can join the meeting, and so the… you see a login screen just in case the meeting is restricted, but the ones for 6 would not be restricted, it would just be, like… Anybody can join.
So it's just, like, if you don't see the Zoom page, you have to click on sign as guest, and then you see the Zoom page. It's… it's the same, it's just…
**Roger Coll** 19:39 Okay, yeah, yeah, it's an extra… sounds good.
Good.
**Pablo Baeyens** 19:53 Anything else?
**Dmitrii Anoshin** 19:59 Oh, thank you, folks.
**Christos Markou** 20:01 Thank you.
**Roger Coll** 20:02 Thank you.
**Dmitrii Anoshin** 20:03 Me too.
Do you know what?
