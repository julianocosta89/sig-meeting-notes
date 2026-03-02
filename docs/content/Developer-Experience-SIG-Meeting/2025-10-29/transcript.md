SIG: Developer Experience SIG Meeting
Date: 2025-10-29
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Damien Mathieu** 04:56 Hey.
**tristan** 05:00 Sorry, lost track of time.
**Perk (Marcin Stożek)** 05:03 I'm on your So maybe, I'll say hello. Hi, I'm Perk.
**tristan** 05:07 Hey, Burke.
**Perk (Marcin Stożek)** 05:08 I just joined Elastic, so…
**tristan** 05:10 Wow. What are you doing for Elastic?
**Perk (Marcin Stożek)** 05:14 I'm a PM for, OpenTelemetry Collector.
and related stuff.
Mostly.
**tristan** 05:21 Thanks.
**Damien Mathieu** 05:22 Hey, Burke.
**Perk (Marcin Stożek)** 05:23 Hey, Diamond. Hey, Tristan.
**tristan** 05:27 Did you join this SIG just because you're looking for different SIGs to check out, or is there anything in particular that you were thinking about bringing to DevEx?
**Perk (Marcin Stożek)** 05:39 So, I'm actually interested in what are you guys doing on the DevEx Sig, because, well, I work mostly on the collector.
And around the collector, I used to, I used to speak at conferences and do some, you know, DevEx around the collector process, so I wondered if I can, help out, you know, in general as well.
**tristan** 06:01 Yeah, the main thing we are working on right now is a collection of blog posts for the website about
production setups of the collector. So, because we ran a…
developer survey months ago, and one of the feedback things was that the docs didn't give,
examples of productionized setups of the collector. So we're interviewing companies and then posting blog posts about how
They run, the collector, both
like, how they're actually running it within Kubernetes or whatever environment they're running it in, but also their company structure around, like, who's in charge of it, and how it interacts with the other teams who are using the collector.
Well, that's our main project right now, and we've got a blog post from Mastodon that we've been reviewing.
And, what's hoping.
Juliano would be here, but maybe he won't be, so that we could discuss that more.
**Damien Mathieu** 07:06 If Daniel could have been here, it would have been nice, too.
**tristan** 07:11 Yeah.
I was hoping he would.
Hmm… So, yeah, I definitely want to figure out what the… user.
User experience, that's the right one, right? Or is it… yeah, it's user or con… user end? End user?
**Damien Mathieu** 07:32 user.
**tristan** 07:34 I mean.
**Damien Mathieu** 07:35 I think, so for, Perk,
basically, we learned that the end user SIG is setting up a project to, do, collector blueprints. Actually, that might be of interest to you. So that, like, blueprint configurations, for the collector, based on actual customer production usage.
Which kind of overlaps with what we're doing with our blog posts, so it's not really the same thing either, and it makes sense for the end user sigk to do that, but we can probably
Mutualize, or share, or, yeah, share…
the work and also contacts, I think.
**Perk (Marcin Stożek)** 08:21 Definitely.
**tristan** 08:22 ones.
What were you gonna say?
**Perk (Marcin Stożek)** 08:24 I just wanted to say that it definitely looks like something that I might be interested in.
**tristan** 08:31 I mean, honestly, I think it sounds like the same thing, except it's missing some things. Like, it's…
It's… we give the… the…
We give both the architecture that they're running it in, and the configuration, but we also provide stuff about how the company is structured, so maybe you wouldn't run it with a demon set, or with sidecars.
If you don't want to deal with these certain things, if you're not this size, things like that. At least they don't cover that in the GitHub issue.
so, I think it could be pretty much the exact same thing, minus a few things.
**Damien Mathieu** 09:09 I think it's a different approach, because we… with our blog posts, even though we can have a list of, like, every company we've interviewed, blog posts are more ephemeral, whereas if you set up a registry of blueprints, then you can actually have, like, a catalog of
just configuration, hotel bin configurations, which is more stable over time, I think.
**tristan** 09:36 Well, it depends, because I agree that if there are approaches to
Keep them updated, then it's very different.
But if…
that seems a lot more work, not on their… both… on their end, which they're… I mean, it's possible to undertake. I'd be fine with us undertaking something like that, but the other end…
**Damien Mathieu** 10:01 It's also something we can say, this blueprint was last updated, like, 5 years ago, or something like that, and then you know that it's probably inaccurate anymore.
But today…
**tristan** 10:12 Mog just says the same thing.
**Damien Mathieu** 10:15 what I mean is that it may be easier for someone just looking for IDs of architecture.
To just have, like, a dump of many companies' architectures, whereas blog posts have a different, goal of, sharing not only the architecture, but how people maintain things, and how they are actually with words, like, using the collector.
**tristan** 10:41 Yeah. Idea. Yeah, you're right that they could work together, and so in that sense, it would be…
When a blueprint gets added to the Blueprint registry, it also has a blog post along with it.
Yeah, yeah.
**Damien Mathieu** 10:59 Or we at least schedule one. Yes, I agree.
**tristan** 11:02 Yeah, yeah, yeah, it doesn't have to be same time, or a block, or anything like that, yeah. Yeah, you're right.
Yeah, hopefully we can talk to him soon.
Because I like that idea.
Okay, and it also means that we have some We have, like, 4… Blueprints for them to…
Go through already, so… they might want to take those.
Okay.
I think it's not joining.
**Perk (Marcin Stożek)** 11:37 Is it you guys who take care of the blueprints, or that's another group? Because I didn't take that.
It's an end-user SEC project. End-user Sikh, okay, thanks.
**Damien Mathieu** 11:50 I think it could be…
like, from discussions with Dan this week, I feel like it could be a joint project, I think. That would definitely make sense.
I think the…
maybe the reason he didn't think of us is that, originally this SIG was kind of thought as a SIG that would look at specification things that were missing, and how we can improve the spec for missing things in the SDKs.
And based on discussions, or, yeah, we…
Have focused on slightly different things, which is improving the experience by improving,
How people can actually understand how it works.
**tristan** 12:38 Based on the survey and limited resources, we focused in on this, yeah.
the… What was I gonna say? The…
Because, yeah, we, in the CNCF thing about How to graduate?
it mentions having this DevX SIG to…
Covered things like the specifications, so we will have to put some focus back on that, eventually.
I think it's partially that our survey didn't do enough to, like, to…
raise those… like, give the users… they said we gave them, like, the free-form area where they could have raised them, but we didn't give enough to, like.
Raise those concerns more.
So that we would know, like, where to focus in the spec. So, I don't really want to do another survey, but we gotta figure out where to focus there, eventually.
**Damien Mathieu** 13:42 And maybe, like, based on the survey, it made sense for us to do those interviews, but maybe, middle term, it would make sense to, like, do, several interviews, kickstart the thing, and then kind of, like, give the baby to the end user sig, so that.
They can continue on that, yep.
Because they have way more people, and yeah, it's kind of already something that they are doing.
**tristan** 14:15 So, and you mean for these?
interviews, we start… we do the ones we've done, and then hand it over to the end user SIG.
**Damien Mathieu** 14:24 I mean, maybe it would make sense to hand over the interviews to the end user sig, and…
**tristan** 14:29 to…
**Damien Mathieu** 14:29 Go back to focusing on specification stuff.
**tristan** 14:32 Yeah, at first I thought you were saying we could do interviews about the specification, because that could be a possibility as well, if we want to find out what people are struggling with.
**Damien Mathieu** 14:42 I mean, maybe the fact that people focused more on lack of documentation maybe was a…
Shortcoming of the survey?
And maybe next time we do a survey, I don't think we should do one now, but maybe next time we do a survey, we should,
focus it more, and show it's more focused on actual miss… things missing in the SDKs.
**tristan** 15:06 Leave out… leave out the collector, leave out operational stuff, or just…
**Damien Mathieu** 15:10 keep the collector, I mean, I feel like the DevExSig could be working on collector stuff.
**tristan** 15:16 Oh, yeah.
**Damien Mathieu** 15:17 So, I don't see why we should leave out the connector, but but it could be just, like, focused on…
Yeah, features missing, in SDKs and collector.
**tristan** 15:28 Right. Oh, it's features missing from the collector as well, yeah. Yeah, if it's focused on features missing, then yeah, I would agree that collector could be included. I just meant to leave out operational stuff.
Okay.
Hmm… Good, good.
Yeah, I think the blog post is…
Looking… good. I want to give it one more read over, but… I was hoping…
Leon will be here, but we can discuss that.
online, get it… get a PR out soon.
Okay.
Is there any more on that we should discuss, or on the blog post, without…
Even though we don't have…
**Damien Mathieu** 16:21 So, for, Perk, we have a draft blog post, our first interview with the Mastodon team.
**Perk (Marcin Stożek)** 16:29 Yep.
**Damien Mathieu** 16:30 And it's… I… we can share it with you, definitely. It's in review. I think we should probably ping,
of the Mastodon folks again, so they can approve.
**tristan** 16:41 Oh, I think he… I think he did?
Because, yeah, they're listed in the, reviewer tracker.
And pinged there. I think he means he pinged him.
**Perk (Marcin Stożek)** 17:00 I definitely would love to… would love to see.
**tristan** 17:03 I'm putting it in the chat, if this link works.
I might not have shared it to you, actually, but let's see if it opens.
**Perk (Marcin Stożek)** 17:16 Thank you.
**Damien Mathieu** 17:23 Yeah, I can't… I don't have access to share it with you.
**tristan** 17:27 Yeah, maybe I don't.
**Perk (Marcin Stożek)** 17:28 And just, yeah.
**tristan** 17:29 That's true.
**Perk (Marcin Stożek)** 17:29 Request… request that the access.
**tristan** 17:32 Okay.
**Damien Mathieu** 17:33 Yeah, you… Giuliano is probably the one… the only one who can do that.
**tristan** 17:42 What's… can you put your email in the chat? It looks like I might be able to do it.
**Perk (Marcin Stożek)** 17:47 Yeah?
**tristan** 17:49 Because otherwise, you'll have to wait on him to… Oh, I got it.
Thank you.
**Perk (Marcin Stożek)** 17:55 Thanks.
Or, actually, the other one. So, should work.
**Damien Mathieu** 18:12 There are… it's a bit misleading, because I think that's something new in Google Drive, Google Docs. There are two tabs, and so the left sidebar is the two tabs, it's in the second document.
If it drops down.
**Perk (Marcin Stożek)** 18:26 Okay.
**tristan** 18:28 Oh, there we go.
Finally sent.
**Perk (Marcin Stożek)** 18:37 Okay, I still don't have to…
**tristan** 18:40 There we go. First, it had a pop-up, what?
Never mind, I cannot share it. I didn't think it let you go that far. If you couldn't share it, it lets me put in the email, click the share button, and then it has a pop-up saying I can't share it. Okay. I thought it just didn't give you the share option.
Good.
**Perk (Marcin Stożek)** 19:03 That's okay. I'll review when, when I have a chance.
**tristan** 19:06 Yeah, once he…
**Perk (Marcin Stożek)** 19:08 Well, once I give it a… yeah, goodness.
**tristan** 19:17 Yep. And is there… Anything else we should discuss?
Okay.
And we can call it here, and hopefully talk to Dan and…
Juliano on… online, and… or Juliano, and…
get the blog post out, and figure out the end-user 6 stuff. Okay.
**Perk (Marcin Stożek)** 19:46 Awesome.
**tristan** 19:47 Thanks, everybody.
**Perk (Marcin Stożek)** 19:49 Nice meeting, John.
**Damien Mathieu** 19:50 Thank you, likewise.
**Perk (Marcin Stożek)** 19:51 Thanks, bye.
