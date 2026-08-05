SIG: OpAMP
Date: 2026-08-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Douglas Oliveira Camata** 00:53 Hello!
**Tigran Najaryan (Splunk Inc.)** 00:57 Hello.
**Douglas Oliveira Camata** 00:59 Oh, I think… I bet some people are gonna be in the old link.
**Tigran Najaryan (Splunk Inc.)** 01:08 It's actually linked from the document, I can also post it in the Slack channel, just in case. Let me… let me do that.
It may be that it's, summertime and people are out, so I don't know.
Let's maybe wait a couple minutes.
**Douglas Oliveira Camata** 02:26 Yes, I think so. August is normally slow.
**Tigran Najaryan (Splunk Inc.)** 02:30 Yeah.
**Dakota Paasman** 03:29 Hello.
**Tigran Najaryan (Splunk Inc.)** 03:31 Hello.
**Dakota Paasman** 03:33 Hindi should be on his way, too, right now.
**Tigran Najaryan (Splunk Inc.)** 03:37 Who? Andy?
Yeah, okay. Let's give him a minute, then.
Andy.
Okay, I think we should start. So, the first one is a change in the spec.
Basically renames files… config files to config objects.
I think I agree with the change.
The, the only question I had was, do we also want to rename the message.
In the… the product, we call it Agent Config File.
And, it would be nice if we could… we could also rename this to be Agent Config Object.
And that doesn't change the protocol compatibility on the wire, because the names of the messages are not on the wire.
It will break… the generated code, the bindings in Go.
But I think it's object, it's, like, it's, it's localized, just maybe… A couple places that it is used, so… I was wondering, what do you guys think?
Generally about the change, and the… what I was saying about the message name change.
Did anybody have a chance to take a look at this PR?
**Douglas Oliveira Camata** 05:38 I think… Yeah, I think it's… Oh, sorry, sorry, Andy, go ahead.
Okay, so, I think that your suggestion, Tigran for changing the name of the fields.
should be fine. I think it makes sense, and it should be fine, because… For the people… bumping the protos, right, bumping their Go dependency to the new version, they will get an immediate compilation error, right? If they were trying to use the old name, I don't know if somehow we could… Oh, we just include the changelog note, they should… just change the name there, and it should be fine. I would be more worried if… Somehow, users would be able to deploy something that would immediately break, but that's not the case.
**Tigran Najaryan (Splunk Inc.)** 06:37 Yeah, yes, yeah, since it's not on the wire, nothing breaks at runtime, it's a compile time change, and as you say, it's immediately obvious. And it's trivial to fix, too, it's just a rename, so… I agree with you.
Andy, you were saying something, or…
**Andy Keller** 07:04 I was just saying, I agree, I think the change makes sense.
And I'm fine with changing the… Name of the protobuf as well, the message, and it's… it'll be a pretty simple… Update.
Where needed, so…
**Tigran Najaryan (Splunk Inc.)** 07:27 Okay.
Sounds good, then.
I saw your thumbs up, Evan, as well, so we're good.
Okay, this one is a bigger change.
And, I mostly reviewed the public API, I think, it works.
There was a small change I wanted to see, it's done, I think it works, so… what we should do next is probably, I'd like to also have your opinion, guys, on what do you think about the public API, once we're happy with What it looks like in the start settings, and what the interfaces are.
Then we can take a look at the implementation, and we'll want the full coverage by automated tests.
But for now, I guess the first step is to agree on what we want the API to be.
Did anybody have a chance to take a look at it?
Okay.
So, please do, when you have time.
I guess Andy and Evan, if you guys also agree with the… with the way the API is structured, we can… we can move forward.
With the implementation, bits and the tests, and all this stuff.
But, essentially, adds, as an optional setting to the start settings.
This one, and that is an interface you can implement either To do a tofu, or without tofu.
And the, the interfaces are… Now, this is the server side, this one is the client side. So this is where you implement it, and these are the interfaces.
**Stanley Liu** 09:29 Yeah, thanks again for the review, and feel free to let me know on the CNCF Slack or anywhere if you have any questions about this.
**Tigran Najaryan (Splunk Inc.)** 09:38 Yeah.
I think that there'll probably be some questions on the implementation. Those will be more like details. What I care about mostly is what it looks like from the public API perspective.
If we're good with that, the rest we can change, refactor, redo, that's not a problem.
**Stanley Liu** 10:00 Yep, that sounds good. I also, I got a review today on the, signing package, so, like, more of the algorithm inserts that you mentioned. I'm not sure if you also wanted someone else to review on that, but I'll be taking a look at these comments and addressing them this week as well.
**Tigran Najaryan (Splunk Inc.)** 10:18 Yeah, this part right here, talking about those comments, yeah.
Is this person also from Datadoc?
**Stanley Liu** 10:26 Yeah, he's also from Datadog. He's pretty experienced with, certificates and, Security, so…
**Tigran Najaryan (Splunk Inc.)** 10:33 Okay, okay, that's good.
Okay.
We're good for now.
So if you guys have a time… Please take a look at it. I guess, Andy, you have a… I really want your opinion on this one, when you have a moment.
**Andy Keller** 10:51 Yeah, I'll get to it, the next day or two.
**Tigran Najaryan (Splunk Inc.)** 10:55 Okay, thank you.
Okay, Dakota?
**Dakota Paasman** 11:00 Yeah, just a quick one. Israel's had this PR open for a little bit now. I think it mostly looks good, just looking for… Another reviewer for it, the package that he is pulling in and making use of.
I'm just not super familiar with it.
So, yeah, just want another reviewer on it. Like I said, though, I think it looks good. It's a strictly additive change. You have to specifically enable the new experimental resource detection in your supervisor config.
So, there shouldn't be any, you know, unintentional consequences from this.
**Tigran Najaryan (Splunk Inc.)** 11:46 This is the experimental package, right? This is the one that you're talking about.
**Dakota Paasman** 11:50 Yeah. Yeah.
**Tigran Najaryan (Splunk Inc.)** 11:52 This is just it, okay.
I think the change makes sense to me, conceptually. I haven't had a chance to look at the… the code, but the concept, I think, is the right one.
**Dakota Paasman** 12:03 Yeah, like, there's one… there was a… environment variable that… Can be set in this… That can be set, and this package will… Basically treat it as the ultimate authority.
When configuring this package, And, like, that was just one thing I found I didn't really know much about in looking into it, and it seemed like there could be an issue if this was set for the collector, but because the supervisor runs on the same machine.
The supervisor would also inherit that configuration, and with this being, like, resource config stuff, it didn't seem ideal that the… Supervisor would have.
the same configuration. You know, maybe in some cases it's fine, but… So that's just an example of part of this package that… I wasn't super familiar with, Just looking for another set of eyes on it.
**Tigran Najaryan (Splunk Inc.)** 13:05 So what would be the alternate? We could, I guess, ignore this environment.
**Dakota Paasman** 13:09 Yeah.
**Tigran Najaryan (Splunk Inc.)** 13:09 in the supervisor. We could unset it or something like that.
**Dakota Paasman** 13:14 I think the alternative is just not using it, you know, I don't think there's a way to configure the supervisor's package to ignore it.
I don't mean to get, you know.
too detailed about this one in particular. It's just an example of… I'm not super familiar with this package.
Something I found that… Didn't feel great about, and… Overall, I think this looks good, I just want another set of eyes on it.
**Tigran Najaryan (Splunk Inc.)** 13:47 I guess, Evan, you probably know the most about this, I'm guessing.
**Evan Bradley** 13:52 Yeah, we just added something either very similar or outright identical in the collector, so I really don't have any major concerns here. I haven't… I've, like, taken a… like, a brief look at this one a couple times, and it overall looks good, but I wanted to make sure that I dug into it and make sure that… I didn't miss anything that would be a little less savory in the supervisor than the collector.
But I'll be taking a look at, like, all of the supervisor PRs that are open right now, I hope by end of day tomorrow.
**Dakota Paasman** 14:31 Cool.
Yeah, that's all I had.
**Tigran Najaryan (Splunk Inc.)** 14:37 Okay, thank you.
That's all we have in the agenda.
Anything else, anyone?
I'm going to be out for the next 3 weeks, so I'm going to miss the next… Sick call.
But I'll be back by… before the end of the August.
**Andy Keller** 15:11 Tigran, do you know what needs to be done to get the calendar invite updated?
**Tigran Najaryan (Splunk Inc.)** 15:15 Sorry, say that again?
**Andy Keller** 15:17 The calendar invite, I noticed, has the wrong…
**Tigran Najaryan (Splunk Inc.)** 15:26 A wrong Zoom link, you mean, is wrong there?
**Andy Keller** 15:31 Oh, you know what, mate? I think I was looking at the wrong… Invite. Maybe it's okay.
I suddenly don't have it in my calendar anymore, so something else happened.
Okay.
**Tigran Najaryan (Splunk Inc.)** 15:41 Well, it looks… looks correct to me in the invite.
Okay, so updated the link in the agenda doc.
Presently.
**Andy Keller** 15:51 Perfect.
**Tigran Najaryan (Splunk Inc.)** 15:51 So, I hope that works.
**Andy Keller** 15:54 Okay.
when I resubscribed, because I don't know what happened, it just… it was there before.
**Tigran Najaryan (Splunk Inc.)** 16:01 Table.
**Andy Keller** 16:02 I'll check.
**Tigran Najaryan (Splunk Inc.)** 16:05 Okay.
Anything else? Anyone?
Alright, thank you all.
**Evan Bradley** 16:17 Hi, everyone.
