SIG: Ruby SIG
Date: 2026-04-07
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/hRH9yM2Q2wdVAADwHpWlxI5-rWz2-vjiVb2Kv8zbLWJ879ndLdMvgUmFe95wkGJ_.piwF_jrWpV6xlyrs
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 01:36 Hi, everyone.
**Hannah Ramadan** 02:34 It looks like you're muted.
**Kayla Reopelle** 02:40 Thank you.
Yeah, so I… I just wanted to see… I was saying that Rob, can't make it and Arielle can't make it, so I was wondering if we're ready to get started.
**Hannah Ramadan** 02:57 Yeah, that sounds good.
**Kayla Reopelle** 02:59 Cool. I'm also gonna turn off my video.
Sweet, let me share my screen.
Okay, so yeah, I'm getting back into the swing of things after being gone for a while.
the… I attended the SPECSIG today. I don't think there's anything that we need to look at straight away.
One thing that kind of reminded me of a recent PR that we had related to HTTP… Response codes is that, there is now a response size limitation to mitigate memory usage risks that was added.
to, just, like, the proto files. I think this will also bubble up to the spec, so we should keep an eye on that. We may need to change some things with our exporters.
Other than that… one other thing that's happening during these meetings now is that they're pulling in folks from SIGs that are focused on different elements of the specification. So, for example, like, the OpenTelemetry collector repos, or, You know, previously, I think, like, the database working group would have been an example of that, and they're having them present at these meetings. So if you participate in any of those other SIGs, you may be asked to present at one of these meetings in the near future.
I guess the only other one that seems worth presenting here, would be… this project proposal to have system packages. This is… Just kind of, like, a wider call to make it a little more… streamline for people to install OpenTelemetry. Right now, you know, there's a lot of manual libraries and manual steps. I think this also includes some proposals to improve auto-instrumentation as well. So if you… I think, like.
All of us here may be from observability vendors, and so kind of more representing users, if you know of users, or you yourself.
and your team would prefer to have a system package like this to install OpenTelemetry.
Highly encourage you chiming in on here, or just adding an emoji reaction. They're trying to find new ways overall to kind of prioritize certain projects within OpenTelemetry, and this is being used as a bit of a case study.
To change the way we're getting feedback, to change the way that we prioritize things, kind of at the… GC and TC levels.
Is there… Anything on here that folks want to look at before we shift to the core repo?
Okay, I'll take that as a no.
Thanks, Hannah.
Was there something that you wanted, or were you just saying good?
**Hannah Ramadan** 06:30 Yeah, just all good.
**Kayla Reopelle** 06:32 Cool.
Alright, I have one item on the core repo, I wanted to check in with some folks about this, requires in the wrong place issue.
So there's a pull request that goes along with this that I've checked out, and I think it's a helpful change. Essentially.
there was an issue with where the requires were happening for the logs and metrics repositories that, kind of forced you to also require the API.
And the larger change in here, that this user discovered was that by not adding require false to our gem files in, you know, even though it's just for test and development, we might not be able to adequately test when our repliers are failing. So, the reason why there's so many files changed is that they're adding require false to all of these gem files. Other than that, there's also… changes to just move where the requires are happening in logs and metrics.
So that you can kind of require the more idiomatic file, of OpenTelemetry slash SDK slash logs, rather than the gemning.
So that's this open PR, but in addition, they also proposed some work… To do a bit of a larger file reorganization.
I think this is going to be a lot to try to talk through synchronously, so this is mostly just to put it on everyone's radar. If you have some time this week to take a look at it, and read through it, I'd be curious to hear your thoughts if you think that this would be a helpful restructuring.
Since we're, you know, still in the experimental phase for logs and metrics, if we're going to make a big shift like this, this might be a good time to do it.
So, so yeah, so I think that's all I wanted to cover on it today. Does anyone have any Immediate questions they want to discuss now?
**Xuan Cao** 08:45 Sorry.
Okay, so for this one, he says, he, he, sorry, I was looking at the code. He, he's saying he, if he required open time GSASH, machines slash, sorry, slash, SDK slash MSX.
Yeah, so… So this one will only require the file called Matrix.
RP, if you do require OpenTeometry, I don't know, hyphen? Hyphen?
**Kayla Reopelle** 09:21 Oh, no.
**Xuan Cao** 09:21 So that will require that, API.
as well. I'm not… I'm not showing that this…
**Kayla Reopelle** 09:29 Right.
**Xuan Cao** 09:29 Is that related to this, his, his, his, concern? Also, his clutch.
**Kayla Reopelle** 09:34 It is in some ways, yeah. The main thing that brought this up to him is that there was an error that came up, this one right here, when… he just required the OTLP exporter And then tried to install the SDK.
And it was this unexpected configuration error due to undefined method meter provider. So, I think his proposal is to be able to avoid manually requiring the API and just, be able to require the SDK and the OTLP exporter.
**Xuan Cao** 10:16 Yeah, yeah, I mean, I mean, you don't need to require API, if you just require the… OpenTeometry, hyphen SDK hyphen matrix will require the API as well. I'm not sure if this… Okay.
**Kayla Reopelle** 10:31 Yeah, maybe… Maybe, would you mind, like, taking a look at this and reviewing it?
**Xuan Cao** 10:37 Yeah, yeah, yeah.
**Kayla Reopelle** 10:38 You're deeper in the metrics. I'll hold off.
**Xuan Cao** 10:41 True, yeah, yeah.
**Kayla Reopelle** 10:42 Merging it or continuing until you can take a look.
Awesome, thank you.
**Xuan Cao** 10:47 Yeah, I'll take it, yeah.
**Kayla Reopelle** 10:52 Hannah, did you have a question, too?
**Hannah Ramadan** 10:57 I was wondering how the other agent maybe, like, required their logs API, if they're doing something similar with, like, the require false, and then just requiring the files.
Of course.
**Kayla Reopelle** 11:11 Yeah.
**Hannah Ramadan** 11:15 But I can, like, it is a big PR, so I can just, you know, add that separately, too.
**Kayla Reopelle** 11:21 Yeah, I think that's… that's an interesting idea, I'm not sure if the ecosystems that other languages use have that same require-false concept, but, it would be interesting to take a look at it.
Okay, awesome.
Thanks for looking at that.
Okay, anything else in Core before we go to contribute?
**Arjun Rajappa** 11:53 A heads up, so I've raised VPR.
I was wondering, like, it should have been a single PR, but I thought, like.
There are 3 different PRs, it would be you to review, so that is why I have 3 different PRs as relates to those.
meeting approach, OTLP… exported into 3D print components.
Just a heads up.
**Kayla Reopelle** 12:18 Awesome.
Thank you. Yes, those, I saw those, I haven't had a chance to take a look at them, but thank you for the heads up. Is there anything in here that you want to go through synchronously?
**Arjun Rajappa** 12:30 No, nothing.
**Kayla Reopelle** 12:32 Okay.
Great. I'll add these to the agenda after the fact, just, So that other folks can see it if they're scanning the notes.
Cool. All right. Hannah, do you want to go next?
**Hannah Ramadan** 12:58 Yeah.
So, I'm looking for some additional opinions on the stable migration for database span names. I have that PR convo and also a Slack conversation link.
And… Where we're at right now is the stable spec essentially doesn't want us to do any parsing automatically for database scanners.
So we wouldn't be looking… doing any parsing for the operation, the table name. Basically, we just want to work with whatever we're given, by the databases.
That is unless somebody opts into this new attribute we're adding called Query Summary. That one is a pretty, like.
heavy parsing attribute to add. There's another PR, probably honestly needs a re-review, so that wouldn't be added until later. So in the stable spec, it's basically either you add this New attribute, or your… adding, like, an operation name, for example, yourself, so people can pass whatever they want into the database span name. The issue with that kind of, like, fallback chain of just using what we're given and not doing any kind of parsing.
is that span names could potentially be a little bit unuseful. I think realistically, if we're not doing any parsing, it probably will end up being a less helpful span name, than what we currently have. So, that's the stable, kind of, like, spec option.
And so what we're doing right now is we have a config that allows users to basically choose what kind of, like, parsing they want us to do. And so we are, at least for MySQL and Trilogy.
**Kayla Reopelle** 14:58 Oh, Hannah, you cut off there. You said we are, at least for MySQL and Trilogy, and then… We went silent.
I still can't hear you.
-Oh, okay. I think we lost Hannah.
I know she's been having some issues with her internet lately.
So, let's maybe wait a second until… Let's see if she can reconnect.
Okay, let's, we'll table this. If she comes back, we can hop into the discussion again.
Let's take a quick look at issues in Color.
Doesn't look like there's anything… New that's been added.
There we are.
Yeah, there's a big release that will go out after this call, big as in just its changes in a lot of different gems. We, are adding the minimum Ruby 3.3 version.
Logs… Exporters, like, our exporters in general are getting some improvements, and then… The metrics exemplars are going out in this release.
I think those are the highlights. We also have some improvements to semantic conventions.
So, just as a… Heads up, those will be out today.
Let's look at… Contrint issues… So we have a lot of good first issues here related to test coverage. This was, something that… James Thompson Tomo discovered recently, that SimpleCov wasn't correctly calculating The test coverage in our results, so it might say that it was passing the threshold, but that was It was kind of checking it at a time that didn't correctly evaluate what the actual test coverage was. So, To address that, he made a few different issues related to gems with known low coverage.
So that that way, hopefully, people can pick those up, and we can bring all of them to our minimum 85% coverage goal.
Oh, I guess this is maybe… A better issue to try to… track things from.
There's also this… Inject key error… okay, it looks like… Sorry, any discussion here?
Also have, a lot of releases going out for Contrib.
I think the majority of these are also related to a minimum… Ruby version bump.
Shane, maybe it's easier to look.
Here… Do we have anything that isn't the Ruby version done?
Nope, looks like it's all related to, just getting aligned with Ruby, now that they've dropped support for Ruby 3.2 last week. Our main versions will all be 3.3.
Are there any other PRs in Contrib that people want to take a look at together today?
**Xuan Cao** 20:51 I don't have money.
Yeah, Except the one, the authentications, yeah, what it is.
I was just reading for Ariel's final approval.
**Kayla Reopelle** 21:06 Oh, this one?
**Xuan Cao** 21:08 No, no, no, the, the other instrumentations, for the operator.
**Kayla Reopelle** 21:15 Oh, for the operator? Yes, yes.
**Xuan Cao** 21:17 Yeah.
**Kayla Reopelle** 21:18 Did that… Wait, why didn't that just show up with you as an author?
Oh, sorry, I just glazed right over it. This one?
**Xuan Cao** 21:30 Yeah, that's true.
**Kayla Reopelle** 21:32 Okay.
Yeah, I haven't taken a look at this one in a while. Do you know what's blocking it? Do you know what needs to happen before we can… Move forward.
**Xuan Cao** 21:46 I don't know, one of Peru language? That's… that's.
**Kayla Reopelle** 21:50 Okay, okay, sounds good. And I'll just add that here.
And I can try to take a look at that this week.
Cool. Hannah, I see you're back.
How's… how's the internet connection?
**Hannah Ramadan** 22:17 Hey, yeah, it's pretty tough. I'm sorry, guys.
I'm…
**Kayla Reopelle** 22:22 Thank you.
**Hannah Ramadan** 22:22 Yeah.
what… What I can also do is… kind of just lay out what I think our options are, for… the spam names, but I would love some opinions on, essentially, moving forward with either trying to Follow the spec exactly, which could mean some less… lesser, like, good names for users.
Or, deviating from the spec, really leaning on that should versus should not language versus must and must not, to give people more options on how their spans are named, including options for parsing.
So, I can, I can put that in the, in our doc, unless anybody has some opinions right now. I've had conversations with Arielle, Rob, and James, in the Slack post attached to the meeting notes as well. That's where you can kind of, like.
read and catch up on where we're at. But, yeah, so if anyone has any opinions right now, I'd love to hear them. If not, maybe you can chat a little bit more about that next week.
**Kayla Reopelle** 23:50 Yeah, I think, I think, chatting next week with, like, a document that maybe lays out the different options that we have, and the pros and cons for them as you see it, that might be helpful so that people can just, I mean, even, like, vote on options, maybe that's a good way to unstick it.
**Hannah Ramadan** 24:10 Yeah, the spec is pretty, Hard to decode, even just, like, all the different options, and… The language on it, so laying it out would probably even help me be able to talk about it better, so I can definitely do that.
**Kayla Reopelle** 24:25 Awesome.
Well, cool. Okay, well, I think that's our agenda. Is there anything else that people want to talk about today?
Fantastic. Okay, thanks everyone for coming, and… I will see you guys next week!
**Arjun Rajappa** 25:08 Okay.
