SIG: Ruby SIG
Date: 2025-12-09
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/3WESAWHc9mTp-kU_Op2GhJM_7HpQWmJd6BuXa4Vr9L9JBigVaLqm4rsd5TOjTWlJ.J1KOjrH0d__y7qm5
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 02:41 Hello, everyone.
**Hannah Ramadan** 02:47 Hello?
**Kayla Reopelle** 02:54 Let's…
Just a second…
Alrighty,
I was out sick most of last week. I'm mostly better now, but I imagine I'll be here this week, so…
I know there's a lot to catch up on, there's a lot that I'm behind on.
That's kind of been a broken record for a while, and I'm sorry about that.
But yeah, so let's… we can start with the Spec Sig, and please,
Add things to the agenda if there's stuff you want to talk about.
And I need to leave at 10.45 today.
So, yeah. Alright, Spec Sig…
So today, there were a couple of big conversations, more like starting journeys rather than… finishing,
We're getting close to merging.
I wonder why this was the link.
Well, there was this whole, you know, slideshow presentation that Carlos did about context-scoped attributes.
And the idea is that, you have attributes
That apply to, kind of, every single data type.
attributes in more places, and that you can potentially use processors and different configuration tools to,
To kind of set those, different attributes.
I think it'll be some time before there's a prototype, but, if you're interested in this, I would recommend watching the recording,
to see Carlos' presentation and the discussion after that.
For this one, there's some different trace state handling keys, that aren't fully supported yet.
I think this is something we should probably take a look at, or at least keep an eye on when it's been merged.
Forget, I feel like we've maybe talked about this before with Ruby.
And then last up was, and I think this was probably most of the meeting, a conversation about providing alternative protocols in OpenTelemetry, so you can't
In this scenario, you wouldn't have to use OTLP. You could use other… protocols,
one of the ideas behind that was, like, a way to extend, OTLP, or to make it more efficient without needing to go through the full spec process.
They didn't imagine there would be a lot of different protocols.
But this was kind of a…
a hot discussion, and if…
you know, you're having problems with compression, or find limitations with the current protocol format, then I'd recommend checking out this conversation.
And that was it. It was just those 3, 3 topics today.
So,
One other announcement, I guess we don't really have an announcement, but I'll post this in the channel. We'll be meeting next week, and then we won't meet, the following two weeks, because all of Hotel is taking a holiday break for the last few weeks of the year.
Yeah, I think that's… that's it.
Schwan, I see you added the exemplar.
That's awesome. Do you wanna… is there anything you want to chat about on this?
**Xuan Cao** 07:24 Oh, yep.
Boom.
I basically just updated everything on this, because this one opened, like, I think 3 years ago? 1 years ago, and then…
a lot of things happens, like, exploding histogram, and then, the asynchronized, instrumentation. So, I just,
I'll update everything, and then… Yeah, make sure they're,
Can integrate with those changes.
And, there is still one, error in the test case, which is caused by JOB, I don't know why.
I mean, if you can help me to rerun it, to see if this…
it's a cost strategy or not, but anyway, I will… .
**Kayla Reopelle** 08:19 Oh, interesting.
**Xuan Cao** 08:20 I'll try to fix this, yeah.
**Kayla Reopelle** 08:24 Yeah, I know JRuby threading can be…
it's different than the standard Ruby. I'll look around in the New Relic test suite to see, because we have some threading stuff,
That might be related to the observable.
engage things. I'll take a look and see if there's anything I can do to help.
**Xuan Cao** 08:47 Yeah, and then I will… I will do some kind of a, like, Real testing on…
Yeah, and then… but meanwhile, welcome to, take a look, and then…
**Kayla Reopelle** 09:03 Okay.
**Xuan Cao** 09:04 Yep.
**Kayla Reopelle** 09:06 Awesome. Thank you. Thank you for updating that.
Alright. And… I guess before we move forward and just dive into PRs, is there anything else,
That people want us to look at, in particular, who are here today.
I actually do have one small discussion topic. I was wondering…
I noticed that there's a pattern that's emerging in the CNCF Slack, that there's often two different channels for language SIGs. There's one that's more of, like.
announcements and help questions, and then there's a different channel that usually is, like, it would be, like, Hotel RubyDev.
that, you know, looks at specifically, like, requests for PR reviews, or discussions about contributions, or, you know, like, people being late to the SIG. And I was wondering if splitting up those conversation streams…
would seem helpful. I know we don't get a ton of posts in the channel, but,
I think I noticed that I'm sometimes hesitant to just post in the main
Hotel Ruby channel, because I feel like…
some of the things that I need to talk about aren't really relevant to everyone who's participating in it.
So, yeah, would anyone else find a channel like that helpful? Do you prefer to have everything in one channel? What do you guys think?
**Hannah Ramadan** 10:39 I like the idea of a split channel, I'm…
I'm starting to think about it from, like, a dev perspective. It would be kind of nice to have, like, a space to go over, like, PRs or tech questions, but if somebody was, like, looking at it from the outside, I could see it being a little more, like, intimidating or, like.
More of, like, a general entry point would be nice.
**Wendy Smoak** 11:01 No, sorry.
just historical open source stuff, like, from Apache, we… There were two… Like, users and dev, always.
And then, so, like, user questions would…
People who are using the thing versus people who are making the thing.
But there's also an argument for not splitting it until it's so noisy that it… It's causing a problem.
**Kayla Reopelle** 11:28 Yeah.
**Wendy Smoak** 11:29 Because you also get…
if you have those dev discussions kind of in a place where people feel like… like Hannah said, people may not feel like they are allowed to write on the dev thing. Yeah.
And it's such a small team that, like, So…
**Kayla Reopelle** 11:44 Okay.
**Wendy Smoak** 11:45 People seeing how the sausage is made might encourage them to contribute.
That's a good point. The split that… I…
was… I don't know if… whether he did it… Ariel brought up wanting a separate channel for
The notifications, like, the automated notifications.
**Kayla Reopelle** 12:02 Oh, yeah.
**Wendy Smoak** 12:03 And that, I'm definitely in favor of, so that it's not… so the humans can talk, and then the machines can…
**Kayla Reopelle** 12:09 Yeah.
**Wendy Smoak** 12:10 Scribble all over the…
**Kayla Reopelle** 12:12 Yeah, I think that would be helpful, too.
**Wendy Smoak** 12:17 Wrong opinion.
**Kayla Reopelle** 12:18 Okay.
Yeah, let's see.
**Hannah Ramadan** 12:27 Do other teams have anything that you noticed?
**Kayla Reopelle** 12:29 Oh, yeah, yeah, so, like, JS has this, I think they're probably more active than we are, but there was another, like.
idea behind this is that the contributor experience SIG is trying to find more ways in Slack to kind of
Point people who are developing things in the right direction, so…
It's been a while since I looked at it, but I think there's some sort of…
Like, automation, that, like, if you… if you join that channel,
They'll also try to connect you to the, like, first-time contributors channel as, like, a way of welcoming and kind of bringing people into the fold.
**Wendy Smoak** 13:07 be nice.
So that doesn't really… So if you don't, it will.
**Kayla Reopelle** 13:11 make sense in the main one, I think. But,
But maybe it does, I don't know. I guess, would that be confusing, to see them in the main channel, too?
**Wendy Smoak** 13:20 It might scare people off.
**Kayla Reopelle** 13:22 Yeah.
**Wendy Smoak** 13:23 Are you joined to ask a question? We want you to do all the stuff!
**Kayla Reopelle** 13:26 Yeah, we want you to build!
**Wendy Smoak** 13:28 If they're planning on automations for it, then yeah, sounds… Interesting.
**Kayla Reopelle** 13:44 Okay, well,
I'll post this in the channel too, I guess, and maybe we can get some other opinions there.
And,
And I can ask about, yeah, the automated notifications channel,
What is it? I think it's the GC.
Okay, cool.
Alrighty.
Let's see… Oh, boy. Okay. So, need to…
Take a look at all these Dependabot things. It looks like there's some linting PRs, and that poor requires PR is way behind here.
On issues… W3C… Random flag…
Someone new, thank you for making this, ticket, Schwan.
And… Don't think we want these to be stale.
Alrighty, oh, and we don't want that one to be stale either.
Okay, let's see, what about in contribib? Does anyone have anything here?
Looks like we have… some more… Managerial things…
Sql Comment Propagator… oh, Ariel mentioned there was a few things he wanted.
looked at.
Okay.
Let's see, Hannah, is this the one that you had taken a look at, too, versus a separate PR?
**Hannah Ramadan** 16:15 I think that's that one.
**Kayla Reopelle** 16:27 Interesting. Okay, maybe this is a good discussion for us to have. So… In the…
I think the version of the semantic conventions that went stable or hotel was something like…
in the 20s, or maybe even the 30s, for, stable HTTP conventions, we could look up the number to see what exactly it is.
But, arielle is wondering if…
We should, you know, move up, kind of, the old convention that we support,
In this whole, like, environment variable where we have,
different semantic conventions that you can choose to send, so that we can hopefully migrate fully over to the stable conventions. So there's a conversation about, like, what should the old convention that we support be?
It… sounds like…
we might want to, it sounds like there's… there's benefits to REL, to kind of increase the old version that's supported to something, more recent, to… to 118.
And up.
But I… yeah, just kind of given where we're at with the semantic conventions migration, I think when we introduced the environment variable, there was, this kind of idea of, like, stability or, like, freezing the conventions at that point in time.
But maybe they were freezed prematurely since the conventions were so old. So, I guess I'm curious about, yeah, what you guys think, and…
Where you're at with, like, changing the spam name specifically to be a version 118 compliance.
**Hannah Ramadan** 18:24 I… I guess, like, what… how I understood this to… or, like, the intention behind, like, the migration is that we would be bringing
kind of, like, just dropping all the old spans and, like, moving forward with the newer semantic conventions.
**Kayla Reopelle** 18:40 So…
**Hannah Ramadan** 18:42 I guess, like, to me, it didn't really make sense to… Go back into, like.
instrumentations as we, like, did them with the old semantic conventions and update those.
cause… like… like, versioning, you know? Like, if someone wanted to, like, lock themselves down, like, that's their,
their prerogative to, like, the old ones and an older Asian version, but if we're, like, pushing everything forward, it seems…
Like, not everyone would want to, like…
be subject to those new semantic conventions if they wanted to stay in an older version, like, so… I mean, I guess, like.
hood… Yeah, I don't know, I guess I thought the point of the migration was to, like, not.
**Kayla Reopelle** 19:28 Yeah. Just to, like, freeze it.
**Hannah Ramadan** 19:29 Yeah.
**Kayla Reopelle** 19:30 Yeah.
Wendy, Schwan, do you guys have any thoughts?
**Wendy Smoak** 19:41 I don't think I'm affected? Does this only affect spans and traces things, or…
**Kayla Reopelle** 19:48 Yeah, yeah, it's only, it's only spans. Okay.
**Wendy Smoak** 19:51 Haven't gotten there yet.
**Xuan Cao** 19:55 I don't have, any strong opinion about the spending.
**Kayla Reopelle** 20:01 Oh, I, I, I just…
**Xuan Cao** 20:03 use whatever, INAP wants.
**Kayla Reopelle** 20:07 whatever is omitted. Okay.
Cool.
I guess…
**Wendy Smoak** 20:16 Preference for being able to be on the latest ish. Thing.
No, we're not… Are you talking about just staying on the old things for a while, or…
**Kayla Reopelle** 20:27 No, it would just be changing, so, I think in…
February, the idea is that we remove this SIMCOM stability opt-in environment variable and release only the stable semantic conventions.
**Wendy Smoak** 20:42 Of course.
**Kayla Reopelle** 20:42 Yeah, for HTTP libraries, so…
**Wendy Smoak** 20:46 So anyone who wants to use the old ones is going to be stuck on a Ruby SDK version at whatever point it still included it, and they…
**Kayla Reopelle** 20:55 Yep.
**Wendy Smoak** 20:55 Yeah. Sounds… Perfectly normal.
**Kayla Reopelle** 20:59 Okay.
**Hannah Ramadan** 21:00 Sorry, can you scroll down to the last comment?
Okay.
Right, because if we merge that, this, this kind of defeats the purpose of the.
**Kayla Reopelle** 21:17 Of locking the.
**Hannah Ramadan** 21:18 the opt-in variable.
**Kayla Reopelle** 21:20 Yeah.
I mean… We could add… another condition, but I don't know, that doesn't really seem compliant.
Yeah, I guess, you know, the hesitation that I have is, Is whether we should have…
confirmed that we were content with the convention that was shared when we,
like, froze it to migrate to the new stuff, since it was so old. But I guess, yeah, I don't know.
Okay, well, we'll continue the conversation in the PR. Thanks, thanks, everyone.
And… let's see… We have some other…
Dropping support for REST client, dropping support for Ruby Kafka… Okay, so nothing… Super new there.
Yeah, is there anything that anyone else wants to chat about?
Okay, cool. Then I will… yeah,
try to catch up and, take a look at that exemplar PR.
I hope everyone has a good week. Thanks, thanks for your understanding with all the…
Being out and sick and stuff.
So… Take care.
**Xuan Cao** 23:10 Thanks.
