SIG: Service and Deployment SemConv
Date: 2026-01-15
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/MUvJmPwl-tCTDN9dBSlpmTtvxpY9RCF6XFzAYcoiL1ldllCh357_kK77JFAEySPS.WoD3zW4ozOckJLhS
============================================================

## Zoom Recording Transcript

**Eimear Foley** 03:42 No. Hi, Deathon.
**Dotan Horovits** 03:45 Hey Mo, how's it going?
**Eimear Foley** 03:47 Not too bad. How are you?
**Dotan Horovits** 03:49 It's fine. Glad to, you'd be… you were able to join.
**Eimear Foley** 03:54 Yes, yes, it's, it's okay, it's only 4PM here.
**Dotan Horovits** 03:58 Nice.
**Eimear Foley** 04:00 What time is it for you?
**Dotan Horovits** 04:02 It's, 2 hours forward, so, 6pm now.
**Eimear Foley** 04:07 Okay, not the worst.
**Dotan Horovits** 04:09 No, no, it's okay.
Hey, Jenny.
**Janhvi** 04:15 Everyone… Happy New Year's!
**Dotan Horovits** 04:21 Happy 2026!
**Eimear Foley** 04:24 A good year ahead.
**Dotan Horovits** 04:28 I have to apologize in advance that I'll have to, leave a bit earlier. I have a double booking on the… on the CNCF… another CNCF call.
With the ambassador team, so,
But that'll be here for the beginning.
**Janhvi** 04:45 Sure, no worries.
Hey, Josh.
**Dotan Horovits** 04:50 Hey Josh, good morning.
**Josh Suereth** 04:53 How's everyone doing?
**Dotan Horovits** 04:55 Good, good, how are you?
**Josh Suereth** 04:59 Pretty good. It, it froze here. It went, like, very cold and snowed. So it was like… we had, I'm trying to think of Celsius. It was, like, what, 10, 11 degree weather? And now it's, like, minus 5 and snowy.
**Dotan Horovits** 05:11 Oh, wow.
That's extreme change.
**Josh Suereth** 05:14 Pretty exciting.
**Dotan Horovits** 05:16 Good day to stay at work from home.
**Janhvi** 05:29 And so I think Trask will not be able to join today.
I don't know if anybody else would be joining. I know, at least from my side, it's a holiday in India today, so I don't think folks would be joining.
**Dotan Horovits** 05:42 Yeah, someone told me there's a holiday, the spring festival, right? Is that okay?
**Janhvi** 05:47 Yeah, yeah, it's… I mean, apparently the winters are now going to be over, and people harvest at this point. Summers are officially going to start here.
Let's do it.
**Dotan Horovits** 05:59 Yeah, it sounded nice. Someone described to me, like, with the rice bowls and everything, like, overflowing, and…
Sounds charming. So I asked them to send me pictures with the, with the outfit and everything.
**Janhvi** 06:09 Oh, okay. Yeah, we… there's, like, a bonfire that happens… that happened yesterday, so that's the festival, and then we eat sweets and stuff like that.
**Dotan Horovits** 06:18 Cool, cool. I did want to take the opportunity also to, welcome Eymar.
MR is from AWS, and I,
I'm really happy being also part of AWS, to have her here, because I do feel that she's much more of an authority, than me, to provide, significant feedback on the, on the matters at hand.
from cloud… cloud of metrics, I think it, speaks for itself, but, I'll let, Ema maybe, introduce herself, if you…
That makes sense as a beginning of the, the meeting.
**Eimear Foley** 06:55 Yes, can do. Thanks, thanks, Jason. I'll do my best to live up to that introduction. Hi, my name's Ymir. Apologies, there's lots of bells in my name, but you can ignore half them.
I am a senior engineer with the AWS Clouds team, primarily in the metrics and alarms space, but I think for the last few years, I've been focused on projects that have let customers discover
telemetry by AWS resource tags, and we're also interested in
Other things, naturally, like Kubernetes labels, resource properties, like the availability zone, and the runtime language, all those good stuff.
So yeah, this is something I definitely have a vested interest in. I'm probably just gonna do a lot of listening today, just to get a feel for how we run these meetings, and kind of… so I can understand better how I can contribute, but super, super excited, and thanks for bringing me along.
**Janhvi** 07:57 Cool, I think, I'll share my screen, and then we can probably get started.
I had added a few things, on the agenda. Guys, feel free to add if you have anything else, that you'd like to discuss. I hope you guys can see my screen.
Okay.
There are a couple of PRs that are up for, review.
Dota and Emer, just for your context, as part of this, we're trying to stabilize a few things, right? And we started with service entity, and with service, we had namespace, instance ID. I know they're already being widely used today, and now we're trying to see how do we stabilize them. They're in development phase now.
Josh, if you remember, last time we discussed that we'll at least send the PRs for them.
Try to have them open for some while and see if, folks have any feedback around that. So I think Arnav from my team, he's added the CRs, added the PRs. I met Yoshi as well last week.
Even he was good with it from his side, so I'd request everybody to review it. I think, Josh, you have a few comments, I'll ask Cardinal to take a look and address them.
But yeah, I just wanted to discuss with this group and see if, you know, you guys have any feedback on that, or if there's anything else that we need to do specifically for namespace and instance.id.
**Dotan Horovits** 09:29 So, on my part, I joined the previous… some previous calls, so I definitely was… it was on my radar, but as I said, I wanted the feedback of the team internally, so I did share both PRs internally, to solicit some more feedback.
And, I haven't heard back from the team anything that is,
critical, but, again, I'll maybe…
refer to, Ima if you want to, comment on that, if you had a chance to look at the PRs, or if you, think that you need more time to review.
**Eimear Foley** 10:01 Yeah, so I had a look at the service namespace and the service criticality, at least. For the namespace, nothing really.
to comment on for me, I think it makes sense to logical with how customers like to do these things. For service criticality, I have reviewed that internally, given
as pointed out, I think, sorry, I don't know who, but someone wrote a really nice doc on the usage of criticality in the Google Docs there. Customers like to use it in the alerting space, and given I am part of Carewatch Alarms, I have brought it back internally to one or two folks, just to kind of have a look, but I don't have any feedback today on that.
**Janhvi** 10:45 Sounds good. Josh, anything from your end?
**Josh Suereth** 10:49 Yeah, so… I think service criticality, I think, is actually good… relatively good to merge, because we have enough appro- well, I think we can get enough approvals, but…
It's broken, the build?
That's why Yal didn't approve it and ask for changes. It literally has nothing to do with the change itself, it has everything to do with the PR being broken.
And so, I guess, do we know… is this someone from your team, John V, who contributed this?
**Janhvi** 11:18 No, they're not from Google. I pinged them offline on Slack as well, I didn't get a reply, I think most probably because everybody was on vacation last few weeks. I'll try to send them a message again on the Slack group that we have.
Let's maybe give them a day or two. If not, how do you recommend we move forward on this one?
**Josh Suereth** 11:40 Yeah, I mean, if all else fails, the… the CL isn't that big, so we could… or, sorry, the PR. So we could make a new PR,
And reference this one to say this is just a cleanup of the previous one, and then get approvals on the new one, and, like, if… so, one of the things with open source, right, sometimes contributors come and go, maybe they gave up and left.
maybe they come back. If they come back and fix it, great, but I still think we should make progress here. So,
if we can at least fix up the build and get things working and take, like, the content they had, I think we could progress with the new PR. That's… that's… I don't remember how long it's been, but I feel like it's been 2 months.
**Janhvi** 12:25 Damn.
**Josh Suereth** 12:25 So, I think that might be long enough that we're… we could consider the PR abandoned and move on to something else. We have a… we aren't as robust with our stale tracker.
on semantic conventions, I think we're gonna be more and more rigorous going forward with that, but
Yeah, in other areas of OpenTelemetry, 2 months is where we start to consider things abandoned and kind of close and reset up.
**Janhvi** 12:51 Sounds good. I think I'll ping them again today. If I don't get a reply in another two days, I'll create a copy of it, and I'll send it back on the Slack channel for approvals and reviews.
**Josh Suereth** 13:00 Yep.
Yeah, if you look at the comments on it generally with that document, I haven't heard of anything that I think is, problematic. Again, it's all…
Unintentional changes and, merge conflicts.
**Janhvi** 13:17 Sounds good. Yeah, I think even when I met Trask last time, he was okay, I think, approving the PR, he just wanted some of the comments to be addressed.
So yeah, let me open it, and then we'll see if you want another copy of the PR or not.
**Josh Suereth** 13:31 Yeah, for context, I approved the PR before they tried to do merge conflicts, and whatever they did with merge conflicts added a whole bunch of stuff I would not approve.
**Janhvi** 13:41 Yeah, yeah.
**Josh Suereth** 13:42 Yeah.
**Janhvi** 13:44 Okay.
**Josh Suereth** 13:46 I have… I have one thing about service instance ID. So one thing, on that one…
With the changes, I'm… I'm ready to approve it, but what… what I think we might need to do, and I need to check, this is stabilizing Service instance ID. Service instance ID is something that, we kind of… there's, like, a secondary task to this.
Which is getting all of the OpenTelemetry SDKs to provide a service instance ID by default out of the box. I need to… I'm looking here, because I don't remember…
at one point in time, someone tried to put that in SEMCOM, that it was a requirement, and I believe I told them, don't do that. We have to put that somewhere else in the OpenTelempture spec, but I just want to check.
Is that under… It's under Resource, right?
**Janhvi** 14:40 Nope.
**Josh Suereth** 14:41 Okay, and this would… I think it's in the non-normative section. Let's check. Service instance ID…
there's a description of it. Implementation such as this case are recommended to provide it, right? So it's not…
Required, cool. So the only thing with service inside destabilizing is we have a recommendation and a should
Around providing this ID. And service instance ID has value when it's consistently provided by everyone, so you can identify, like, the source of data. So there's a piece of this that I think we want to advertise with the maintainers in OpenTelemetry.
So, like, the OTEL Containers Group, or the OTEL Spec CNCF Slack channel, or those SIGs, just to say, hey, this is now stabilizing. Those of you who weren't implementing it, because you wanted it to be stable, like.
Make your comments now, because once it's stable, we're going to have this as a recommended pattern that all SDKs provide the value.
**Janhvi** 15:35 I see.
So, for that, we'll first have to talk to the maintainers group. Is there, like, a forum where we kind of send that PR and then ask them about this? Like, what's the process around it?
**Josh Suereth** 15:47 It's very informal. Again, we have… so OpenTeLens, we have a lazy consensus model, so unless somebody complains about something and it's been open long enough, you can merge it.
But as a, as a, like, you know,
what do you say? A benefit to other people in the ecosystem. There's an OTEL-maintainers chat channel that you can post it to, and say, hey, looking to stabilize this, we… I'll approve it, so it looks like it has approval, but we can say, like, that we think this is good to go. If you have concerns or things, please let us know.
You can also do… there's an OTel-specification channel in CNCF Slack, that's another place you can ping.
To… to get folks to just take a look. This is one of those, like, courtesies to everyone of… yeah. It's also possible that what… what I… what I want to have happen is everyone says, this is amazing, thumbs up, can't wait, right? You might get somebody who says, hey, I have concerns, here's what it is, but,
I think that that was already addressed, because we advertised the change to service instance ID.
Well before this, so that was, like, a year ago.
**Janhvi** 16:58 Okay, yeah, I think that that makes sense. We'll get feedback also, and just if somebody has anything to say, we can get that and incorporate it in the PR. I'll have Varnav, who's the author of the PR, he's from my team, I'll ask him at least, to send this one. Do you think the namespace thing, we should send that as well in the group and just get feedback from folks?
**Josh Suereth** 17:17 I would fix the namespace PR, because when I looked at it, it was… it was just…
**Janhvi** 17:23 Yeah.
**Josh Suereth** 17:23 but it was the service instance inside HPR.
**Janhvi** 17:27 I'll get that done as well.
**Josh Suereth** 17:29 Yeah, there's also merge conflicts now in this. Okay.
**Janhvi** 17:35 I see. Okay. Yeah, we'll get that one fixed. Okay.
**Josh Suereth** 17:39 Yeah, one thing I'll warn you about with SEMCOMF, we unfortunately get a lot of merge conflicts.
I don't know how we can… we need to find a way to sort that out, but a lot of these PRs need active, merge resolution, or we get approval, then we do merge resolution, then we, submit.
**Janhvi** 17:59 Hmm.
Okay.
Sounds good. I'll get this one fixed, and at least for this one, we'll send a message, on the group and see if we get any feedback. Dota and Ymir, also please take a look and let us know if you have feedback on any of these, and then we'll wait it out for some time, and then we can eventually, hopefully, merge it.
Alright.
There's one more PRH. Let me open it up…
Oh, I think, Josh, I saw this one, I think you had sent this earlier. This is for the owner attribute.
And looks like they're adding this in the development… Mode, is it?
**Josh Suereth** 18:46 Yep
Yeah, this is from Jurassi, from the Governance Committee of OpenTelemetry, not part of… I don't think he's participating in the SIG yet, but I just wanted to, make sure we're aware of this, because I think this might have been on the,
the original proposal as well. Yeah. Yeah, so, I'll briefly be the champion for it, even though I haven't evaluated it yet in my head.
So, yeah, this is basically… any service can have an owner, that owner can be a name, like a URL to represent who that owner is, and that sort of thing, and a contact.
for this PR, like, when I was looking at this PR, name makes total sense to me, contact communication makes sense, but also, like, we have this weird thing with OpenTelemetry about,
Including and non-including PII.
So, I feel like… I didn't look at the details, but I feel like that should be an opt-in kind of thing, where there needs to be some level of control of whether to include that.
Where I think the owner name might be less…
PII, like a team name is fine. A actual email address for a team, maybe not. I don't know, but maybe they're the same.
Again, I haven't thought through it, but the things that I think we probably need to discuss are, like, is this the right set of attributes to represent owner? Is that the right meaning for URL? It lists as the source code repository or docs.
Could… could URL just be, like, a link to information about the owner?
It, like, as a description.
I want to make sure the description isn't limiting, but is sufficient and something that we want. So, I think, John, being your original proposal, there was, like, talking about having an owner.
But I don't remember it having this level of detail. So,
I think that just talking about, is this the right set of things to start with, again, for development attributes.
it's lower weight, but I would prefer to have these descriptions be flexible, because this is such a generic concept myself.
And then just, is this the right set? I think this is a very useful set, right? Knowing who it is, how to contact them, and then, like, a place to go to get information about them seems useful.
**Janhvi** 21:07 Yep.
**Josh Suereth** 21:07 I don't really know if I'd want to send that on every, like, log or trace or,
You know, metric.
But having it as, like, something you could attach to a resource if you're reporting resources independently, that makes sense to me, too.
**Janhvi** 21:26 Yeah, I think on a high level, I agree that the owner thing makes sense, but I'm not very sure. For example, I think the URL says services, source code repo, or documentation, right? So that doesn't really make sense for me.
I know at least in Google Cloud, right, at least, Josh, you might know this, for AppHub.
we… I know there is an owner thing, and that's also compounded into, like, multiple things. I don't think… I mean, it has nested fields, I'll have to look into it to see what all is represented there, but maybe we should do that exercise the way we did for criticality, right? In general, how is owner used in open source, in other clouds?
And then maybe we can see what are the fields that we would like to have in hotel.
**Eimear Foley** 22:09 Yeah, I think that was kind of where I was leaning when looking at this, because oftentimes when, like, speaking with customers, owner means quite a different thing for them. It could be the team, it could be the financial owner, it could be the business unit.
Whereas this is very much scoped down to almost like an engineering or a DevOps-type use case of owning the team, which might make sense when you're looking at logs and metrics and traces, but I… I think owner is quite a overloaded term, in a sense.
**Josh Suereth** 22:43 The other thing I'll call out, this is creating a new entity.
So, like… In the new entity model, which isn't complete, you'd be able to report this independently of service?
So, you could have, like, all my metrics report what service they are in, and then there'd be a separate channel that could say, this service is owned by this thing.
And on that entity relationship, you can actually put attributes. So you could say, like, this is the financial owner, or this is whatever.
since that model's still in flux, like, we have to be careful designing against things that don't exist yet, and the way things work today, this would all just get shoved into resource, so I think,
Anyway, I agree with you, like, owner is… generic.
And anytime we have these super generic things, I'm fine with us taking a little extra time to get the right model here, you know?
D-do you have a…
So, John V, and, sorry if I mispronounce your name, is it, is it Amer? Emer?
**Eimear Foley** 23:47 Emer.
**Josh Suereth** 23:48 Emirt, okay, eMERT. If you have, like, a list of how you're using Owner that is shareable.
I think the first thing we should do is get that on the PR, of like, hey, here's, like, an actual use case we have for ownership, and the things that we include, and then we can do a mapping between the proposal and what we need to provide, and try to make sure that, you know, if we have a reasonable modeling of all that stuff fits here, great.
If we can't… Then I think we make some changes.
It sounds like we might need an owner role here. Like, there might be multiple owner types or something.
**Janhvi** 24:25 Yep.
**Josh Suereth** 24:25 Yeah.
**Eimear Foley** 24:29 Yeah, I think… sorry, that actually triggered something in my brain. I think oftentimes, like, for our customers.
it is billing use cases, like, they want to know who… who omitted those metrics, logs, and traces, so who's… who's causing me all this money?
Whereas, like, that's not always necessarily the team who owns it. Yeah, I can definitely speak to our product team, I think, and, internally, we have, like, our tagging org, so, I think I can talk to Scott about that, Doughton.
**Janhvi** 25:02 I think I can do the same thing, at least from our end. I know,
So, I'm part of the tags team in Cloud, right? And, before we started working on this proposal, the product manager that we have here, they kind of went out and talked to a lot of customers who use Google Cloud, and we wanted to understand… we wanted to understand what were the use cases where they're using some of the commonly used tags. Owner was among the top 10 that people were using today.
And the use case that they were using owner for was mostly billing-centric use cases. They wanted to, like, group resources by the owner name, and they wanted to figure out the spends for that specific usage, for that specific owner. So that was the major use case that we had, gotten at that point. But I can do a deep dive again and see, how they're using it right now, if there are any additional use cases on top of it.
**Dotan Horovits** 25:54 I'm just wondering if also, I know that in the SEMCONs in general, we try not to get these blurbs of extras, but since it's such an overloaded term, if we can actually provide
Such a short list of closed list, without having something to accommodate for.
extras. So, again, just thinking out loud, even when we cross-reference the different, use cases, it would probably be either a very, very long list that, that doesn't, like, it's a superset of everything, or we sort of get these, sort of, baggage of, of,
Use case specific, let's say, owner details.
**Josh Suereth** 26:36 Yeah, that's a good point. That's what I'm trying to avoid. Like, so I think there's two things. One is, if it's a bag of labels, we can add more over time if we find we need to.
But I also would like the initial model to not require that. If we know of the use cases ahead of time, and there's a way we can model something where, like, a short amount of labels can apply to a bunch, let's do that. But let's also not overfit, right? There's always overtuning. So, I think both are true, there's a bounce.
But if we know about the use cases, we can make better decisions now, so let's make the best decision we can, and I do expect these to evolve. Like, I actually really like that, Jurassi made an entity where we can have multiple labels in case new use cases show up. We're not limited, right?
Anyway, the important thing here for everybody is, let's get our comments on the PR as much as possible.
So, because I… yeah.
Cool.
I have to drop in 5 minutes, and that's all I had for today.
Apologies, I've been distracted.
**Dotan Horovits** 27:42 I need to drop off Nina as well, so… Apologies.
**Janhvi** 27:48 Sounds good. Even I don't have anything else on the agenda, so we can probably… Eymar, if you also don't have anything, we can call it off, and then we have a few ways we can work on it.
**Eimear Foley** 27:58 No, I'm all good. I didn't bring anything to the party today.
**Janhvi** 28:02 No worries, sounds, sounds good. Thanks, everyone. Thanks for joining.
**Josh Suereth** 28:06 Thank you.
**Dotan Horovits** 28:07 Thanks, everyone, have a good day.
**Eimear Foley** 28:08 Thank you, bye-bye.
