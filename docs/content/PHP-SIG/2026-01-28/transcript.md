SIG: PHP SIG
Date: 2026-01-28
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/DQQlRR2E3uIUpfrVTlC9y7LLaDnba8K9RcsI8mHCRXLqLcihsRO6Qx8quBMiIPCN.0uEGn1FpNysploRm
============================================================

## Zoom Recording Transcript

**Sergey** 00:11 Hello.
**Pawel Filipczak** 00:13 No, it is.
**Chris Lightfoot-Wild** 00:15 You know what?
**Bob Strecansky** 00:20 ferns.
**Chris Lightfoot-Wild** 00:23 Well.
**Bob Strecansky** 00:24 How y'all doing?
**Chris Lightfoot-Wild** 00:27 Good, thanks, Olivia.
**Bob Strecansky** 00:29 Living the dream.
**Sergey** 00:31 No glasses?
Type into the glass.
**Bob Strecansky** 00:33 Yeah, I had… I had tennis practice this morning, so I'm… I don't… when I'm playing, I can't wear them, so… you're catching me right… that's… you're catching me right afterwards.
**Chris Lightfoot-Wild** 00:48 Excellent.
**Bob Strecansky** 00:49 Alright, let me pull up the agenda… Oh, how's your vacation?
**Pawel Filipczak** 00:55 Great.
**Bob Strecansky** 00:56 Not long enough.
**Pawel Filipczak** 00:57 Great.
What?
**Bob Strecansky** 01:01 Good weather on vacation makes it.
Makes it all.
**Pawel Filipczak** 01:05 Yeah.
It was 50 degrees difference between Poland and Italy, so… yeah.
**Bob Strecansky** 01:12 50… 50 degrees C, or 50 degrees out?
**Pawel Filipczak** 01:15 Sears, Celsius, yeah.
**Bob Strecansky** 01:17 Oh!
**Pawel Filipczak** 01:18 So, yeah, it was minus 15 here, and it was 15 there, so…
**Bob Strecansky** 01:24 Whoa!
That's… that's, not… that's not fun. It is, like, minus 10 here right now, and I just feel like an icicle all the time.
Alright… Today… Alright.
Alright, so, does it… Does anybody have any, top-of-mind items before we get rolling on the agenda and the boardwalk?
**Chris Lightfoot-Wild** 02:03 Only the thing, well, you tapped Sergey in an issue last week, I'm not sure if you've seen it yet. Yes, I saw it.
**Sergey** 02:11 Sorry, I didn't have the time to take a deeper look at it, but I saw you referenced me, I will take a look at it.
**Chris Lightfoot-Wild** 02:16 Cool. Thank you.
**Bob Strecansky** 02:19 Guess what?
Oh, that's this one… All right, my update for this week is I worked with the other maintainers and disabled Dependabot. We are now a renovate-only rep… Grouping of repos. Thank you, everyone. That was more annoying than it should have been. But, that should spam our channels a little bit less with automated updates.
If nothing else, we can go and look through.
**Chris Lightfoot-Wild** 02:50 Oh, can I add one more thing to the… sorry, just, onto the bod. There's the V2 branch. I was just curious… We can discuss it later, at the end.
Yeah, it was more like, what's the state of it? Like, obviously, I know Brett's away, but there's loads of stuff happening in, like, V1, like…
**Bob Strecansky** 03:11 Yep.
**Chris Lightfoot-Wild** 03:12 surgeon, and… Good.
**Bob Strecansky** 03:14 I mean, I don't think we have anything else we need to talk about, so we can… I mean, that is pretty pressing.
**Chris Lightfoot-Wild** 03:20 Yeah, there was, like, a…
**Bob Strecansky** 03:23 Not me care.
**Chris Lightfoot-Wild** 03:23 there's a… I'm sorry?
**Bob Strecansky** 03:25 Possibly, tell me your feelings.
**Chris Lightfoot-Wild** 03:28 Well, mate, it was more like, obviously, last week, Cedric had opened a PR against Maine to sort of introduce new ways of loading things, which kind of… I think SPI covers, and then, like, the move toward that is more prevalent in V2.
And then there's a divergence, obviously, that it… if people aren't necessarily aware of the SPI stuff, because they're not coming to these meetings, and then they just sort of, you know, look at… check out main and go, this is how it works now, I'll just copy that, build my own thing.
Obviously, you don't want to upset people in, sort of, say you're doing it wrong, but we've deviated, and… Yeah, then obviously I've seen Nevis sort of swinging on that PR, and he's opened another one to… you know, again, it's against men. I'm just wondering, like.
we're muddying the waters a bit by having V2 and… Not moving toward it.
**Bob Strecansky** 04:23 It's a very solid question to raise, Chris.
I think the right answer to that is… We should.
merge… we should merge that V2 branch at some point. I think that… I think that we should probably have a, like, a public forum discussion about that in OTELPHP, and get… make sure Brett sees it, and make sure that we get, like, Neveh and, Cedric and some of these other, like.
I don't want to call them power users, because that's not the right… maybe it is the right word for it. OpenTelemetry PHP power users are aware of it, and think about… make sure that It's not going to break anything that they're currently doing, whatever, so… I'm happy to start that discussion this week, because I think you're right, like, it's been long in the tooth. We have to rip the band-aid off at some point, but we have to determine when that point is. And I think that point could be now.
**Chris Lightfoot-Wild** 05:18 Yeah, I think, especially, we've dropped 8.1, or there's a PR that's imminently about to do that, and that seems like a sane time, if any.
To ramp up toward, you know.
B2 of the package as well.
**Bob Strecansky** 05:33 Sounds good. I will start a discussion about that, today.
**Chris Lightfoot-Wild** 05:37 Awesome, thank you.
**Bob Strecansky** 05:39 You're welcome.
And we really… I really value your input there, too, Chris. Don't think that you… that it's a decision that goes without you, so…
**Chris Lightfoot-Wild** 05:47 No, no, no, I'm more of a casual user, I think, so…
**Bob Strecansky** 05:52 I think you're a little more than a cat.
**Sergey** 05:53 But are we absolutely close on it being necessity for it to be, like, a breaking major version? Because then… I don't know, maybe it's already done. Then we will need to have some transition period for the instrumentations, right?
To kind of, like.
They also will be all upgraded to a new major version, or they'll be somehow made Compatible with both major versions.
**Bob Strecansky** 06:21 I think that will be extremely dependent on the implementation. My guess is we'll have to update them all eventually as well.
Just, if no.
**Sergey** 06:33 Because I remember Brett mentioning that the breaking change was kind of like an internal API, Used by instrumentations.
Oh.
**Bob Strecansky** 06:43 Yep.
**Sergey** 06:44 But we absolutely can, like, 100% that we want that API to be considered, kind of, like, public, and breaking it… requires introducing…
**Bob Strecansky** 06:54 I think If you have these issues, Sergey, let's raise them in that… thread that I'm going to start today. I don't… I don't think we have all the people that are really necessary here to make this decision, so I don't want to make decisions…
**Sergey** 07:07 Eventually, we can avoid a lot of overhead of introducing new major version, and then maintaining all the potential, combinations that needs to be maintained, but okay, I will… so, is that issue already exists, or you, you'll open the one?
**Bob Strecansky** 07:22 It's not an issue. I was going to raise it in, I was going to raise it in the OpenTelemetry PHP Slack channel. If you prefer it to be an issue… So, an issue may be a better… what do y'all think? Would you rather see an issue, or would you rather see a Slack channel?
**Sergey** 07:36 It doesn't matter personally, but maybe if you think it should be public, and searchable, then Issue will serve that better.
**Chris Lightfoot-Wild** 07:44 You could always link to it, obviously, in Slack as well, couldn't you? I'm sure everyone that's interested is already on Slack, but passers-by were more likely to just go to GitHub.
And… Yeah, maybe…
**Bob Strecansky** 07:55 Maybe that's a good point. Maybe it's not an either-or, maybe it's a both. It's… I think that's probably a big enough thing where we should… we should probably have an issue that links to the Slack discussion.
We can do that.
Okay.
That's what we'll do.
**Sergey** 08:14 By the way, do we know what other teams do? Like, do they consider API between instrumentation?
**Bob Strecansky** 08:20 I have no idea.
We could find out.
This is the, let's start walking the board. Chris, this is the other PR that you were talking about with… for Nevae, yeah?
**Chris Lightfoot-Wild** 08:40 But, yeah, I think that was the one that he's linked to, 1867 was the comment he put on Cedric's.
**Bob Strecansky** 08:47 Oh, I see.
**Chris Lightfoot-Wild** 08:47 Whereas introducing some… like, using the registry, which is what I think is… Been removed in, V2, I think.
**Bob Strecansky** 08:59 Okay.
**Chris Lightfoot-Wild** 09:00 But yeah, it's just… That'd be good to… to link to that as well, I guess, as a case in point, and see what, What the general sentiment is.
**Bob Strecansky** 09:09 Yeah, I'll link, I'll link this in our, in that issue slash Slack thread.
And this one, too. So…
**Chris Lightfoot-Wild** 09:18 To be fair as well, I've not checked the V2 bunch, I mean, I think Brett may… may be keeping on top of it, but obviously, Yeah.
**Bob Strecansky** 09:26 Yeah, he's…
**Chris Lightfoot-Wild** 09:27 more mobile.
**Bob Strecansky** 09:27 He's been on paternity leave, and I'm sure his attention is divided at best, so…
**Chris Lightfoot-Wild** 09:33 Oh, yeah, absolutely, so yeah.
**Bob Strecansky** 09:35 on it.
**Chris Lightfoot-Wild** 09:35 Additional overhead, does it?
**Bob Strecansky** 09:38 I don't wanna… I don't wanna assume that he's been keeping up with… I've seen him lurking in the shadows, but I don't want to assume that he's, I want to assume he's doing nothing, right? Like, we can't expect him to do things when he's not available or online.
**Chris Lightfoot-Wild** 09:52 Oh, yeah, of course, yeah.
**Bob Strecansky** 09:56 Alright, so these are just… Renovate bought.
Trib had a couple.
This is the PHP 8.1 and PHP 8.5 thing you were talking about. There are a couple other open ones that we should probably review.
And then instrumentation, probably all renovated, too. Yeah, these are all renovated, so I'll get on those as well.
Our backlog, there's nothing really relevant anymore.
Alright, road to SDKv2 is… Looks to be completed, so that's good, that's a good leading signal that we should… release 32 at some point soon.
And we are continuing to go up, except for Christmas time. Thank you for pointing that out, Les, that's okay.
Alright.
Is there, what else is on people's minds?
**Sergey** 10:55 By the way, just to refresh my memory, what is our policy regarding the PHP releases support? We end support when the PHP officially ends support?
For each lesson.
**Bob Strecansky** 11:04 There's, I think it's in, the README, let me find it. There's, like… I wanna say it's, what, like, a year after release or something like that?
Support…
**Chris Lightfoot-Wild** 11:15 Yeah, that was one where I mentioned the same thing as well, I think, the other week. The wording suggests within a year, and… Yeah. Quite quickly within that year. Yeah. Yeah, I mean, PhD versions just go, like.
**Bob Strecansky** 11:28 they go burr, so we have to be very conscientious. And we said… Brett and I said this a long time ago, we can change this if we decide we need to. This is just the compatibility promise that we've promised our developers currently. If we change this, we would have to be very verbose and conscientious about it, but it's possible. It's not like… this isn't a… Unfortunately, OpenTelemetry doesn't have, like, a generalized support vector, because there are lots of languages like Java, and Java wants to support, like, Java 8. And, you know, like, some of these things that will live in enterprise infamy forever. And, you know, like.NET wants to support Windows XP, Yeah, it's just, like, some of these… these goofy things that… are, like… That make it difficult to make a standard on what your support pattern should be, so it's kind of like a best effort, but… I think it's just… I think, to me, this is a good pattern currently, but if we need to change it, we can, we just need to be, like, extremely verbose in the fact that we're going to change it.
**Sergey** 12:31 Maybe it's worth clarifying, can you please click on that link on the supported versions of PHP, the visual table? What is considered to be end of life, because it's a little bit confusing.
it shows that 81 is end-of-life, but We say that we will support year… additional year after end of life, right? If understood correctly.
**Pawel Filipczak** 12:52 Yes.
**Bob Strecansky** 12:53 I think… I think… I think the most important thing is probably the security support. Again, I don't think that… I think that… our definition is loose, probably on purpose, but, like, the security… once it's done with security support, that should probably be a pretty good indicator that we shouldn't support it anymore.
But… I don't know.
**Sergey** 13:15 So, I consider it to be… so essentially, this is… I guess this is how this table works, according to what you said. I think they show now 8.1 to be end of life, because security support ended. We don't see it at the table, but I assume…
**Bob Strecansky** 13:27 it had security support until the end of 2025, right? Yeah.
**Sergey** 13:32 is for us that we need to support it one year more. Excuse me, Chris, please go ahead.
**Chris Lightfoot-Wild** 13:36 Sorry, I was just saying, there is a link there, a table of end-of-life branches, just above the table you're looking at. I just think it was…
**Bob Strecansky** 13:44 Yeah, so…
**Chris Lightfoot-Wild** 13:47 Very keen to get rid of it in 2025.
**Bob Strecansky** 13:49 Yeah, so, yeah, so this is end of life 28 days ago, and so…
**Sergey** 13:56 It's a little bit confusing, it doesn't say explicitly end of life, right? So it says unsupported.
Okay.
**Bob Strecansky** 14:01 The unsupported end of life, same… not same difference, but same difference for the.
**Sergey** 14:05 Let's assume that this is so… yeah, it sounds like… let's assume that… so that means that we need, according to our own, decision, to support it for one more year, right? 8-1.
**Bob Strecansky** 14:18 At most, we need to support it for one more year. The way that word… that wording is… is… it says… And support will be dropped within 12 months of that version going end of life. And end of life, like you said, end of life is not listed here. This is no longer supported, and those are two different things. Maybe that's just bad verbiage.
**Sergey** 14:38 Although in the link, they mentioned end of life, so it's a little bit confusing, but I assume this is what they mean, right?
It seems that they're used interchangeably.
**Bob Strecansky** 14:47 We shouldn't be supporting PHP 3.0, that's for sure.
**Sergey** 14:53 Right. Although, I must say that, saying that we will drop it in the, in the year, like, it's… it's not clear then whom this promise is made to, like, is this promise to developers that they need to be taken care of 81 anymore, or is it a promise to the customers, to the users of the… of the product? Because, then users need to guarantee, you know, minimal amount. They don't, it doesn't help them that you say, okay, I will definitely drop it within the year, but then if it will be on the first day of the year, it doesn't help them much. They need to understand if it's at least a year or not.
**Bob Strecansky** 15:25 That's a really great question, Sergey. I don't have an answer for you.
**Sergey** 15:30 So this… I understood it, but yeah, you're right, the way it's phrased in English, within 12 months, means that it's a max, it's a limit on the top, not on the bottom. So, Yeah, I guess, I would probably change it to be on the bottom, hmm?
**Bob Strecansky** 15:47 I think also the intent with that is to be flexible. I think being pedantic about the, like, the phrasing of this is not important. I think the important thing is, like, if we see a bunch of end users that are continuing to use 81, and they, like, make requests for us to keep supporting it, and they have, like.
really important, like, again, very subjective, but, like, if they have quote-unquote important needs for us to maintain 8-1, we probably would do it. But if we… if we say, oh, we're end-of-lifing 8-1, and nobody, like, raises a red flag or questions it, then we're gonna do it, because like, it's expensive to maintain old versions of software, as you all know, and I don't want to get in the business of maintaining, you know, 2, 3, 5, 10-year-old versions of PHP.
for an observability library, but if we have to, then we have to. So, that's my opinion. I'm very easily swayed here.
maybe we need to take a better… maybe we need to take the opinion, like, guess what? It's not supported by PHP anymore, it's not supported by us anymore. Or maybe we need to be on the inverse of that, and be like, well, we… if it's been on… if it's been released.
Like, if it's… if OpenTelemetry PHP has had a version that's been compatible with your version of PHP at any point, then we have one that will continue to be compatible at any point.
But, I don't know, I think we have to be very careful in walking this line, because it signs up people for a lot of undue work.
**Sergey** 17:11 No, no, I think the point is, I agree with your just former approach, that you say, okay, let's align ourselves with the PHP cadence itself, and it sounds reasonable, right? To be saying, okay, this is what Upstream decided, and there is no reason for us to invent something new.
I'm just saying that this additional year that we take as a buffer, I think there is only a reason to it only if we guarantee it. Otherwise, there is no point of mentioning it. Then we can just as well say, if this is our intent, we can drop it immediately after end of life by Peach Pizza, then let's just say that, like, then people will not even count on that.
**Bob Strecansky** 17:49 You're right.
I think you're right. I think perhaps we should… raise an issue to discuss this, and probably ask Severin, too, because he's our PHP GC liaison, and maybe he'll have some insight that we don't.
**Sergey** 18:05 We can, of course, use what you also said, I mentioned that we can take the statistics, right? We can say, okay, let's see if even it's been… if this is even a factor, maybe it's not even used the way it wants, then…
**Bob Strecansky** 18:17 Then it becomes kind of like a mute point.
So, moot point, yeah. So, like, if you look at our versions, we can see… let's see, so, like… Wow, 8-6, look at that.
We can go and take a look at some of this. This graph is really annoying to read, but… So, like, here we can see… We still have… Like, a very, very small number of our users are… less than 8.2, what, it's like 10%? That's… that's not zero.
**Sergey** 18:54 But I would probably not count even 7, so if we're just talking about 8-1, so 6%.
Yeah.
I don't know, I guess it's worth discussing, is it, is it valuable percentage? Like, what is the percentage that we'll consider to be…
**Bob Strecansky** 19:10 Yeah.
**Sergey** 19:10 Good.
**Bob Strecansky** 19:11 I don't think anybody's really thought about this, realistically. It's just like, yeah, we'll do our best to support it, right? We're all… We're all volunteering to do this on our own time, so I don't think that there's any, like, explicit guarantee But I think now it's becoming to a point where people are expecting specific levels of support. We want to be able to give it to them if we can, but I think, yeah, let's… let's open an issue and talk about this, because I think I want to get feedback from the community at large to see, and from Cedric, too, because I think that he'll have some valuable insight here.
**Sergey** 19:44 Right. I guess from our point of view, like, if we're coming from corporate point… interest point of view, obviously for us is the traditional stability obviously simplifies things for us, and as long as we would like to position this project as something that can be, you know.
widespread and used by corporations as well, enterprises, then stability will become important for them, right? They will be less, They might suddenly become, you know.
It's… I guess that they, they have, slower, kind of, like, pace of change in the version. Although, obviously, I agree with you that claim can be made that they are opening themselves to all kinds of security exploits if the PHP itself wasn't really not supported anymore, so… That's also cool.
**Bob Strecansky** 20:28 Thank you.
**Sergey** 20:28 Yeah.
**Bob Strecansky** 20:29 I think you have the theoretical, and then you have the practical, right? Like, theoretically, you should update every single app that you have to every new version of PHP immediately when it gets released, and so on and so forth, but… In reality.
**Sergey** 20:42 I can open an issue. I think you're right, probably worth, probably, we probably don't see… all we discuss now is the… is the benefits of keeping it. Now, it would be interesting to understand what is the cost of keeping it.
**Bob Strecansky** 20:53 What are the costs? I think, like you said, we need, we need to make a data-driven decision here, not a heart-based decision.
Because, like you said, it does… it does cost time and energy to maintain older versions, and if we don't need to, based on data, then we shouldn't. And if we do need to, based on data, then we should.
**Chris Lightfoot-Wild** 21:16 Could I ask, sort of… position, I guess, that you might have better insight into from an elastic perspective, then, like, with your… older agent, what typical support would you have given outside of end of life, if any?
**Sergey** 21:34 I don't remember, I guess it's public… Pablo, do you remember what is the guarantee? I think after we declare… obviously, if we declare the cadence, the cadence, like, if we're running the cadence in advance, but I think the requirement to at least report it for a year after we declare the end of Of life, or something?
**Pawel Filipczak** 21:50 Right?
**Sergey** 21:51 Fuller?
**Pawel Filipczak** 21:52 We don't have any statement about that, so if we decide to drop support, we have to just announce that.
**Chris Lightfoot-Wild** 22:00 Right, okay.
**Pawel Filipczak** 22:01 But, you know, we have to give sometimes, sometimes for the users to adapt or to migrate.
But here, we don't have any statement in our docs so far.
**Chris Lightfoot-Wild** 22:16 Sorry, go ahead.
**Pawel Filipczak** 22:19 We was discussing this support period until we agreed at some time that it should be one year after, but of course.
Depends.
**Sergey** 22:27 But I think, in general, Elastic does commit to supporting certain technologies, like, after providing, like, declaration that something is end-of-life, there is some minimal period that we need to continue supporting that.
So, I just need to find out what is that minimal. And obviously, if we know the cadence in advance, we can already kind of pre-declare and say, okay, we already know that the end of life will be at that particular date in the future, so… Yeah. So, for us, it will be the question of, obviously then, We will need to find a way to whatever will decide here in OpenTelemetry itself, versus whatever will Elastic commit itself as a corporation.
We'll need to find the… How much buffer it will require us to…
**Chris Lightfoot-Wild** 23:12 The knock-on effect of, like, the distro, for example, like, because obviously you support 8.1 in that currently as well, don't you?
If you… if we're gonna say 8.1 is end of life, then… The distro comes out, and you've got 8.1 in there.
you know, it might be confusing, or if we've just come out with it and say, and this.
**Sergey** 23:31 Well, it depends, like, distro, after it will become upstream Distro, then it will be aligned with whatever policy we'll agree on. We will not keep it 8-1 if we decided that 8-1 is unsupportable.
**Chris Lightfoot-Wild** 23:41 Now, we will also have an Elastic downstream version of the distro.
**Sergey** 23:46 And it, we can continue supporting it one, if this is what Elastic committed to, right? So that's… that's already on us, this additional buffer, whatever we'll have to buffer as additional time, you know, that we committed to our customers, that will be… but, Let's first make a decision, like Bob said, based on the data that is concerning to us as a project, and then whatever feedback we have as a corporation, we'll bring it on. It might have some value, but it definitely will not be, you know, some decisive factor, so… but we will bring it, yeah. It's all public, we're not hiding it, yeah.
**Chris Lightfoot-Wild** 24:23 Cool, thank you.
**Sergey** 24:30 Okay.
So, would you like me to create an issue in GitHub to discuss it?
**Bob Strecansky** 24:35 Okay.
I think that's the best place to do that. Let's do it. I'm excited to see what other… But, make sure you tag Severin in it, because I'm interested in his opinion, too. Or I will, if you link me to the issue.
**Sergey** 24:47 Okay, okay, I will send it to you. Okay,
**Bob Strecansky** 24:50 I'm interested to see.
Cool.
Thank you for doing that.
**Sergey** 24:55 No problem.
**Chris Lightfoot-Wild** 25:01 Sounds like that's a wrap, is it?
**Bob Strecansky** 25:03 That's a wrap. We'll see y'all on the internet.
**Chris Lightfoot-Wild** 25:06 Cheers, though.
**Sergey** 25:07 Guys, bye.
**Chris Lightfoot-Wild** 25:08 Bye-bye.
