SIG: Ruby SIG
Date: 2025-08-19
Duration: 52 minutes
Zoom Recording URL: https://zoom.us/rec/share/Db5Jl5ZRTdwMBdLHvtHVe-VbR6SkLcwHuQxmhZc5_rxa_6TpUbu5u1lCHEc1EmqO.gpAMDlB2Vmg235U4
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 02:34 Hello, everyone!
**Eric Mustin** 02:44 Hello?
**Kayla Reopelle** 02:45 Hello, hello.
**Eric Mustin** 02:48 I can share the… I can share the dock to be….
**Kayla Reopelle** 02:52 Nice, that'd be great.
**Eric Mustin** 02:53 useful.
Good.
Thank you.
Okay, … Alright, I assume you can see my… Screen.
Oh, cool, today's.
August, 19th?
Okie dokie. … Do you want me to pull up the specs, and we can…
Timebox it for a few minutes, if you attended?
**Kayla Reopelle** 03:45 I did go, yeah, so we can do that.
**Eric Mustin** 03:50 Oh, wait, what?
Oh, no. Oh, yeah.
**Kayla Reopelle** 03:55 And brought up an issue from our, repository in a second.
**Eric Mustin** 03:59 I'll let you dry… apologies. I'll let you dry the cadence, but here's the, … alright. There it is.
**Kayla Reopelle** 04:05 Hmm.
Yeah, so, not…
a whole lot that I think was really relevant, to the SIG as a whole. Some things are…
They're changing the…
process up a little bit for how we track, what specs have been implemented. It'll be in a YAML file now.
the… attribute, value types, PR, I think, got merged today, so…
this new extension isn't actually breaking anything. Yeah, that's the… The spec compliance matrix.
**Eric Mustin** 04:42 Amlified, new, new word.
**Kayla Reopelle** 04:45 Yep.
**Eric Mustin** 04:47 I love it.
**Kayla Reopelle** 04:48 Their goal, kind of, in the future, is to have files in every single, …
like, language repository that holds this information, and have updates of those files, you know, to, like, add new lines about the specification, get added through automated PRs.
But that's, you know, still up for discussion. So if you have thoughts about that, I think this issue would be a good place to put them for now.
The other discussion about things that might change is that there could be a, …
a new symbol in the future that kind of denotes the separation between the implementation being marked stable and the implementation being present, because right now, there's only one symbol that represents both of those things. So I'd kind of hesitated from
updating the Ruby spec compliance matrix because I thought we needed to be stable in order to add the new attributes, but I found out that that's not the case. So, later on in the meeting notes, I have a link to that, matrix update PR.
The next one, … was a discussion about an issue that Wendy opened, last week, I believe.
And… yeah, this ability to find metric instruments after they're created. There's kind of, like, two parts here. Being able to find the metrics instruments, like, from the registry, and then the second part being, removing instruments from the registry at some point, kind of like how you can unregister a callback.
There was an old issue, hadn't been worked on for a while.
about removing, the instruments that got brought up again, and I think
It was just kind of too last minute for the people who had worked on it previously to have any sort of
context to jump in today, the general sense was that this was just abandoned due to, like.
lack of time and abundance of distractions, rather than, like, a desire to avoid implementing it. So I think there's still interest in this, and .NET has some partial implementation, so, …
if, …
you know, if we're interested in trying to further this, I think, you know, we could consider implementing the feature as well as just another
Kind of example, and just marking it as experimental.
…
on the topic of something like exposing some sort of instrument registry. This is something that Erling is doing right now.
And, so their implementation could be a good example, and they started doing this just based on it being, I think, difficult or maybe impossible to have global variables in their,
In their language.
But the recommendation was to go to the Developer Experience SIG and, kind of talk about this issue there to find out how other people are managing this right now, or if this is a problem that other users are facing. I have a conflict this Wednesday at 11, so I can't personally join, but if anyone else wants to bring the issue forward there, you can find the link to join the meeting on the OpenTelemetry Community Repo.
Yeah, I think that's pretty much it. The other topics that came up were about updating file-based configuration for,
The… for authentication, and the last issue….
**Eric Mustin** 08:19 Sorry.
**Kayla Reopelle** 08:20 Oh, it was about, the trace ID ratio-based sampler, and kind of trying to move along another old issue that had been, frozen, so possibly renaming that, ….
**Eric Mustin** 08:33 Yeah.
**Kayla Reopelle** 08:33 sampler, deprecating the existing one.
I think, …
it will probably still be a few more cycles before that one gets merged. So if you have thoughts about it, now would be a great time to join the conversation.
**Eric Mustin** 08:50 Cool. That was a great 8 and 8 in 7 minutes flat. That's a new land speed record, I think, for the specs.
Yeah, it'll be interesting. The sampling one looks like there's some pretty concerted effort to do… you know, it's a big project, though sort of like, I guess they're…
the… the next version of whatever sampling looks like in a hotel. It seems pretty large, so I'm sure there will be a lot of, … yeah, it'd be good to… if people have strong opinions.
Seems like they definitely have bodies working on it, but it's a lot of work, and I don't even know the full scope of it.
Yeah, I mean, I, … that's good to know, I guess, about for us specifically, about the… I'll go back to the Ruby, notes. I can't… I can't join the SIG, I don't think, but it's interesting that there's an implementation out there.
But it's… as I understand it, it's not like that implementation was merged into the spec or anything, there's just, like, a… that was an example of what they might have used for, like, an OTEP or something, if people wanted to pursue it.
….
**Kayla Reopelle** 09:54 Yeah, and so I think the door was kind of left open for people to read and reflect on it, and maybe talk about it a little more next week, after people have had a chance to review, but it could maybe make more sense to wait until the following spec sig when I have a chance to actually go to the Developer Experience SIG and bring those findings back.
**Eric Mustin** 10:13 Mom.
Yeah, I, … Gosh, it's so hard to, like, …
you're like, I don't know, I'm just on a ramble. But I feel like, it's like you're Mario, and you get to the castle, and it's like, oh, actually, Prince of Peach and the other casters, like, go to this other SIG, and, like, listen to a bunch of people talk about problems you don't care about.
**Kayla Reopelle** 10:29 Oh, yeah.
**Eric Mustin** 10:30 So, but cool, cool, glad it's, appreciate you going, to the, the specs again.
**Kayla Reopelle** 10:36 Yeah.
**Eric Mustin** 10:37 Yeah, awesome.
Yeah, I mean, we don't, … if no one else has spec specific things, we can…
you know, we've… we got all the time in the world now. We can move on to what's listed in quarantine Tribe. If people have pressing issues they want to bring to the front, you know, I'm happy to, you know, I think we're all flexible.
Okay, I guess we'll just start with core. Alright, Kayla, you have a issue….
**Kayla Reopelle** 11:03 Yeah.
**Eric Mustin** 11:04 PR.
**Kayla Reopelle** 11:04 that I opened. When I was looking at the spec compliance matrix, I noticed that I had spelled the environment variable incorrectly for adding long record attribute things, there's no underscore,
In between log and record.
However, like, one question that I have is whether, you know, since this implementation is still in development, we could easily have breaking changes, does it make sense to keep the version with the underscore, or should we remove it and only have the, like, documented spec-compliant one?
… I'm kind of curious about what people's thoughts are.
I mean, of course, we would, like, mark it a breaking change if we removed the environment variable and kind of call that out in the changelog.
… But, I know….
**Eric Mustin** 11:54 ….
**Wendy Smoak** 11:55 That's a user.
**Eric Mustin** 11:56 Oh, yeah, yeah.
**Wendy Smoak** 11:56 me, if you just change it and put it in the… in the changelog, it's… I mean.
That's one of the things you get by not calling it 1.0, you can do whatever you want.
**Kayla Reopelle** 12:06 Hey, great.
**Wendy Smoak** 12:07 So why… why put yourself through all that trouble if you're not going to officially, you know, call it done?
**Kayla Reopelle** 12:15 Okay.
That's… sounds good.
**Eric Mustin** 12:19 Oh, I just approve it quickly. Yeah, I mean, if we're…
I think our user base for logs is relatively… is still, accountable by hands and toes, so we might want to just, you know, rather than have to maintain it and do the weird cadence of, like, flipping, you know, introducing it with off, flipping, like, yeah, I'd rather just kick it off.
**Kayla Reopelle** 12:40 Nice. For me, I mean… AR.
Before, … Before we merge. But yeah, thanks for the approval.
**Eric Mustin** 12:48 Other one here is spec compliance matrix, right? You were talking about that. So, when you were saying these symbols… I'll let you, sorry, I'll let you talk. Is it the symbols in that, like, actual table, where it's, like, a star and a plus and a minus and, like, a….
**Kayla Reopelle** 13:04 Yeah, exactly. So, like, the plus is just, like, implemented in any form. Here, I'm gonna pull up the matrix itself and drop a link in the chat, or… yeah, you can kind of tell there.
**Eric Mustin** 13:16 Well, this is, like, sorry, the.
**Kayla Reopelle** 13:17 I would like that, yeah.
the….
**Eric Mustin** 13:23 File? Is that how it works?
**Kayla Reopelle** 13:26 There we go.
**Eric Mustin** 13:27 Okay, yeah, no problems, I don't know what you changed.
**Kayla Reopelle** 13:31 Oh, yeah, I think if you go back, there's, like, a button you can press to look at it and mark down with the diff.
**Eric Mustin** 13:39 Really?
**Kayla Reopelle** 13:40 If you click on that little file symbol to the left of the viewed checkbox on the file.
**Eric Mustin** 13:46 ….
**Kayla Reopelle** 13:48 So if we look at the file… Viewed, viewed file, whoa, rich diff, right.
**Eric Mustin** 13:52 That's what that is.
**Kayla Reopelle** 13:53 Yeah.
So that should show us the lines have changed, maybe?
**Eric Mustin** 13:58 Yeah, the entire table.
**Kayla Reopelle** 14:02 Wow, the entire, the entire table.
**Eric Mustin** 14:04 Okay, I think we can… whatever.
I can live in just regular….
**Kayla Reopelle** 14:10 So, I think, we need some sort of Ruby…
other Ruby representative approval on it, probably, before they merge.
I only noticed one missing feature with Tracer. I think I have…
pretty much everything that was checked off for metrics. There's a few…
Things we might need to, like, update still.
But if anyone else wants to, like, take a look at it.
check my work, that would be great. I did minuses right now, ….
Or some things that I know we have, like.
PRs for, but we haven't added them yet. I thought that might help make things a little clearer, but….
**Eric Mustin** 14:53 Yeah, yeah, yeah.
**Kayla Reopelle** 14:54 add my pieces on everything that we definitely don't have. Right now, that's just my own little key of, like, oh, this is a PR I need to review.
**Eric Mustin** 15:02 Right.
I, thank you for this. I think, yeah, I don't, Schwan, you may want to review some of the metrics ones, you would might, you know, or I guess Wendy as well, you've been close to it, if you happen to have the time. I can, I guess, touch a couple of these, but…
I wouldn't even be able to say. I think it's better to… I mean, like, I think there's, like, the content marketing aspect of, like, like, if you have a…
like, AWS is a distro, of Ruby, so, like, I don't know, maybe they have opinions, but, like, it's fine by me to market. Let's be honest, straightforward about what the state of the state is, sort of, and then, yeah, I think it helps
It would be nice if you could have, like, a little, asterisk to be like, and here's the link to the PR related to this, but, like, they'll find it. It's better to call it out than say it's unknown.
**Kayla Reopelle** 15:51 Right, right. Python does have links to PRs for some of their, icons, so we can….
**Eric Mustin** 15:58 I guess we don't even… yeah.
**Kayla Reopelle** 15:59 If we want to, I'm happy to add that. There's not too many PRs, I think, to add right now.
**Eric Mustin** 16:05 I'm fine with… I think it's fine to market as whatever to, you know, use your judgment on whatever, you know, level of granularity you want to put in here. I guess sometimes it could also then be confusing, because then, like, maybe in the future we won't maintain that standard of excellence, and people assume that there isn't a PR, but actually we just release the…
So I don't know. It's cool. I, … I think this will help a lot with adoption, so… great.
**Kayla Reopelle** 16:30 Nice, excellent. And I think this kind of instigated the Yamlify PR, so I don't know. It might get more difficult to add links in the future, too. But yeah, logs are on here as well. There's just a few features missing from logs.
… Hmm.
That I sent telephone to, so….
**Eric Mustin** 16:53 Okay.
**Kayla Reopelle** 16:54 Yeah. Awesome, ….
**Eric Mustin** 16:56 Okay, I, …
I know I just keep, you know, I'm just going back to the well, but, you know, Kayla, do you want to contribute and just go through the other….
**Kayla Reopelle** 17:06 You only have.
**Eric Mustin** 17:08 7 more issues.
**Kayla Reopelle** 17:09 Yeah, you know, it's only… oh, I guess one other shout-out on the core is that, I will merge the new release today for the Metrics SDK, so that'll come out later today.
And while we're talking about releases as a segue to contribib, there will also be releases there. I'm gonna close the current release PR, because we need to bump the rails of instrumentation into all instrumentation, so I figured I would just try to do that as separate PR and get everything released at once.
… Huh.
**Eric Mustin** 17:42 Is there… are we bumping rails because rack's getting the… The….
**Kayla Reopelle** 17:46 If Support has some changes. Okay.
For as part of the rack updates, so that's why we're bumping rails.
Or not Active Support, Action Pack, yeah.
**Eric Mustin** 17:57 That works for me.
**Kayla Reopelle** 17:58 Controllers, or whatever? Yeah, yeah. Yeah, exactly.
**Eric Mustin** 18:01 Probably because the naming is bad. ….
**Kayla Reopelle** 18:04 The… but it does segue into this other… the first PR, I guess. So the CI workflows had been slightly broken, so there were a couple of releases I thought had gone through, but did not, and those have all been taken care of now. But the problem, was kind of with this new app token that we were moving to.
It didn't have repo permissions, I think it had… I forget what permissions it did have, but this new token will have repo permissions.
And so that, this should solve the problem, fingers crossed, but if we can get this merged before I open that new release PR, that would be a good opportunity for us to test it. The workaround, if anyone does, like, need to do a release through the, like.
Just the standard…
request release action? I think that's what it's called. You just need to add the release pending label to the PR that gets created, and then that will tell Toys to kind of finish it, and remember to add the completed label when it's done. So we do have a viable workaround.
But … yeah, I think if we get this merged, we won't have to worry about that.
**Eric Mustin** 19:14 Cool. I approve it. I think we need one more, maybe, but maybe I'm sure Ariel may want to look at it.
Cool. Oh, right, right, that, right, … Working here. …
other things? Or, yeah, I don't know, anyone have, … did anyone want to have, … we've kind of been…
Flying through, so just, you know, speak up if there's, …
Otherwise, we'll keep going, I guess. The smaller PRs I had seen….
**Kayla Reopelle** 19:47 Do you want to just go through them?
**Eric Mustin** 19:48 Now, and see if what we can….
**Kayla Reopelle** 19:50 Fair. Yeah.
There's just a few cleanups kind of related to that release. So this one, you know, since the gems weren't actually released on the days that I thought they would be, this PR just updates the changelog for accuracy.
And I have an invisible, unfindable markdown extension that deletes spaces, so that's in there too.
**Eric Mustin** 20:15 All good. Hey, you know, we're saving… doing God's work, we're saving bites, it's all good.
Alright.
Group that, I guess? Huh.
I think it's fine to modify the, …
You know, I don't think there should be.
**Kayla Reopelle** 20:29 Yeah, I think so. I don't think toys… I don't think it'll bite toys.
Oh, that's the one. Yeah, I guess I forgot I had already been on….
**Eric Mustin** 20:38 163, yep, and then this last one is….
**Kayla Reopelle** 20:43 Oh, I was… so there was a new PR that's opened, to add some Puma instrumentation, which I think could be a good one to discuss if we have time.
And, …
I just noticed that there was a comment in there that's inaccurate for our process now. We now declare our development dependencies in the gem file, kind of as a reaction to a RuboCop default change. So, yeah, let's just clean the left.
**Eric Mustin** 21:13 Should we… Changed… toys? Or I guess you're already….
**Kayla Reopelle** 21:18 The generator got changed in here, so it shouldn't, be a problem for, like, future… Oh, okay.
**Eric Mustin** 21:24 Okay.
Sorry, I'm dumb, I can't see it, but I believe you.
**Kayla Reopelle** 21:28 What is the instrumentation generated? That's the first file.
**Eric Mustin** 21:31 Okay.
Gotcha. Okay, right, right, right. … Good catch.
I think I should just do this when I see the email notifications.
**Kayla Reopelle** 21:45 But there's so many emails. Thank you.
**Eric Mustin** 21:49 Thank you, Arjun.
Okay.
And so concludes the core contrib… the agenda… the formal, you know, stuff. I guess, you had some happy reports you wanted to share as well?
**Kayla Reopelle** 22:04 Oh yeah, just some other shout-outs. So yeah, we got instrumentation all released now with the new SEMCOMF opt-in variable PRs that Hannah was working on. We just have releases for RAC and the HTTP remaining for HTTP conventions, so that, like, opens up the possibility for
adding, you know, stable conventions that weren't present in, older instrumentations, we could do that now.
You know, we can kind of start that… we're about ready, I guess, to start that 6-month timer to pull out the triplicate.
**Eric Mustin** 22:38 Yeah, yeah, yeah.
**Kayla Reopelle** 22:40 So yeah, I think this is a big step, and something we've been working towards for a while, so I just wanted to shout that out.
**Eric Mustin** 22:46 Yeah.
**Kayla Reopelle** 22:47 And, on the core side, asynchronous metrics have been released, which is, like, a lot of work that Schwan did, and so this has been a long time coming. The PR, you know, I think 90% of it has been finished for many, many months, and so I was glad we were able to get
The other elements of it out to the world for users.
And I'm hoping that I'll have some time this week, too, to look at some of the other, long open PRs to get them moved forward as well for metrics.
**Eric Mustin** 23:20 I, you, you're our mensch, doing, you know, all the… appreciate all the heavy lifting here. Yeah, awesome, awesome work, Anna. What is this? I guess we'll keep an eye on, we'll know who to… who to, annoy if there's a suddenly, like, you know, a bunch of people are like, hey, my Ethan instrumentation.
**Kayla Reopelle** 23:39 Right, right.
**Eric Mustin** 23:41 No, it should be. I think the…
you know, the verbiage is pretty… I think we're pretty loud about everything going on, so…
I think we'll only… we'll probably hear about it in 6… whatever. I'm sure that will be the long tail of people.
**Kayla Reopelle** 23:56 26 months, yeah.
**Eric Mustin** 23:57 Yeah, or whatever, but … but, you know, that's… they should upgrade. … Cool, … Yay.
Oh, ….
**Kayla Reopelle** 24:06 I don't want to put you on the spot, Hannah, but we could talk about the database stuff.
But if you don't feel like it's ready, you don't need to.
**Hannah Ramadan** 24:15 Yeah, … Yeah, I can… I can talk about it. So… Last…
week, or the week before, I was talking about how we had to add some new attributes for the database, libraries.
And I was a little concerned, because some of them required some parsing, which in the past I've gotten some, like, hesitation about, like, what that might do to performance.
There is… oh yeah, thank you, Kayla. Kayla just shared the issue in the chat.
**Kayla Reopelle** 24:56 I guess that's the general one. I think we have one for…
the issue you're talking about, unless I misspe.
**Hannah Ramadan** 25:04 Yeah.
**Eric Mustin** 25:04 Sorry, I was trying to….
**Kayla Reopelle** 25:08 Oh wait, there it is. Sorry, my bad. Here's the other issue.
**Eric Mustin** 25:11 dbuquer space?
**Hannah Ramadan** 25:11 Nice, yeah.
**Eric Mustin** 25:12 That one, yep. Cool.
**Hannah Ramadan** 25:16 Yeah, so when I was starting to look at, adding that opt-in variable for database instrumentations,
that one's kind of blocked now based on this attribute. So, db query summary is set to be the name of the span, as well as, like, an attribute. And it requires parsing, like, there's just kind of, like, not a way around it. When I chatted with, one of the .NET
like, Asian authors, they implemented this, but the way they did it was…
by basically running all SQL queries through one parser, and that gave them an obfuscated
Query, as well as generated this query summary.
I want to probably follow the same pattern that they're doing.
It's kind of weird because, like, if someone, for example, like, has obfuscation turned
off, like, they don't care. We're still kind of generating it. Either way, we'll just not send up an obfuscated query. So it's kind of like an interesting, like, we're always going to get, like, that, both of those things generated, but hopefully it won't be, like.
that much of a performance hit. I think if I base all… base the… pattern off of .NET, …
should be okay. I put a post in the…
Slack channel, just in case, like, to bring up any conversation about, like, how this is working. I… I'm not sure if it really, like, would be a performance concern. Arielle in the past, like, kind of mentioned something about…
a performance hit when I was trying to add another attribute that required parsing, although that was regex, and I think that
… this… the Donna implementation is a different pattern.
So, hopefully it'll be okay. I just wanted to bring this up in case anybody has any concerns before I get started on actually, like, writing the code. Might also be easier to review.
Or let's talk about once there is code in place, so that's also fair too, but if anyone has anything that, you know, this strikes them as, like, odd, or things to, like, talk about before we get started, we'd love to just, to chat about that.
**Eric Mustin** 27:37 … I can, …
So, yeah, yeah, it sounds like .NET has, like, a, … it's like a lexer, like, it tokenizes the SQL queries, and then there's, like, a lexer, …
There is some prior art.
from other… there's some Apache 2 implementations of, like, similar things, not in… …
tell native conventions, but basically Datadog has a… Datadog has a package in Go that does this, and…
at some point, there may have been an attempt when I worked at Shopify to, like, turn that into an OpenTelemetry processor, collector processor, and it was, like, a really hard implementation.
But, so good luck. It's hard, yeah, writing, like, a…
Lexer and Tokenize is, like, good… it's, like, a good project for sure, but it is, …
There, there may be some other… I pinged you in the Slack of, … they have a… they host a… it's a separate Go module or whatever that they've abstracted out of the Datadog agent, and you can see, like, their implementation. I think it's based on…
Whatever the, …
it came out of… whatever the MySQL thing is that, PlanetScale runs, whatever their… I'm sorry… Getting old.
… Anyway, … Yeah, there's some, … so there's some prior art there, but it's, … I, …
I just… I, … I wanna save you a lot of pain if you can't, like, if there's another, … I don't know. It's a… it's a big undertaking, and… but I don't want to…
tell you not to, you know, I think it's just something you can implement. Like, it's not, it's not, like, some unfathomably impossible bit of engineering. But yeah, that might help as well, because I don't know, you're familiar with .NET relative to Ruby, relative to Go, relative to, like, some other things.
So…
Yeah, you know, like, I don't know .NET at all, and I actually still don't really know Go, but I have to write it sometimes. But yeah, yeah, you might want to use both of those and kind of see what they're doing. And I would say, like, be… if you're… if you're doing,
like, before you get too far down the rabbit hole, you might want to, if you have an initial implementation, just see how it compares to, like, a regex approach of just, like, a pile of regex, which is what we've been doing. You may find that, like, that, you know, like, I think some of the reason, at least in Go, they went down that route of writing Alexis, because Go's regex engine is really bad.
So you might be able to… yeah, you might just save yourself in trouble and be like, oh, you know what, like, let's just, you know, I'm not gonna get a big performance win out of doing it this way, although I… I think…
it seems reasonable that you could write, you know, you could optimize the Alexa. But yeah, maybe see if there's… if it's worth the effort, and if not.
Just kind of try to pile of regex plus feature flags, so you're only calling it when people, you know.
as minimally as possible. May, sort of like what we do… basically what we do now in, some of our other, like, you know, obfuscation things. See if that's, …
Just don't, don't throw that on the ground yet. Basically validate early that your, the lecture's worth the effort.
Anyway, I'm sorry, I'm rambling. I have PTSD from attempting to do this, and then Francis being like, your implementation sucks, and then me having to not do it, and then I got fired from Shopify. So, yeah, anyway, good luck.
**Hannah Ramadan** 31:06 No, that is actually really helpful. Yeah, I… I'll take a… you said you tagged me in….
**Eric Mustin** 31:13 In… it's in Slack… I'm just in the Slack channel. I dropped a link to the repo for the Go implementation of it, …
And… I guess it's not, it just tokenizes the queries. You can see, like, I'm sure they pull the… if I… if I bet… if I had to bet, if you find that package, if you were to go into the Datadog agent, I bet they're pulling in that package to do…
Some more specific… Obfuscation. I think the, you know, the tricky part is, like, …
To me, this sort of, like, summary, it'll be specific on the flavors that we, you know, like.
what flavors do we want to… is it just MySQL?
**Kayla Reopelle** 31:50 Postgres, you know, like, what flavors are….
**Eric Mustin** 31:54 Sure.
**Kayla Reopelle** 31:55 databases, I don't think it applies to, like, NoSQL databases.
**Eric Mustin** 32:00 Yeah.
Plastic, or something.
Or Mongo, or something, …
Cool. Yeah, I would say, I think the Datadog one may have a lot of that stuff, like, crammed in there too, so I don't know. …
Because it's cool.
…
cool, … I think it's… I think it's a good, … sorry, just to get back to it, like, I think it's good to try to add some of these if we can, …
I do, …
Yeah, I wish, I had some more feedback from the field of, like, what's… what are people actually, like, banging on the door that they really want?
Of, of these fields, versus, like, oh, this is just, like, this income.
**Kayla Reopelle** 32:38 And the tricky thing with this one is this is the spam name in the stable convention, so we need.
**Eric Mustin** 32:43 Oh, really?
**Kayla Reopelle** 32:44 This year.
what the span name has become. The… the old span name is, like, option 3 or 4 in a tree, if you can't get this. So this is the… this is what is….
**Eric Mustin** 32:56 Right, because they want to….
**Kayla Reopelle** 32:57 They want to generate, like….
**Eric Mustin** 33:00 I get it. They want to do, like, metrics, be able to do, like, red… use metrics on, like, the queries, obfuscated queries, you know, like, summarized, you know, quantized queries, so they're, like, oh, let's make that the default spin name.
**Kayla Reopelle** 33:13 Yeah, so that's why it's more important to make it performant, is that… or, like, some sort of config tree.
**Eric Mustin** 33:19 Okay, yeah, yeah.
**Kayla Reopelle** 33:20 Because, yeah, even, like, I think what Arielle had mentioned in Slack is that he's planning to use this collector component, which might be the one you were referring to, to do the sanitization moving forward, so he doesn't have to worry about the reject, but we still bumped into the parsing problem because of a spam name.
**Eric Mustin** 33:40 Sorry, you're not gonna watch open telemetry. Sorry, there's, … that did remind me. There is a…
Oh, right, collector, I'm sorry.
not work? … the core logics What is my brain? … I think it's CoreLogix?
Has this feature that they shipped a… I'm sorry.
…
Not doing a great job here. There is an implementation in the collector you may want to review as well. But again, it's Go. It's all, you know, so….
**Kayla Reopelle** 34:23 Let me see.
**Eric Mustin** 34:24 … But in this processor, it's called, like.
Am I… is it CoreLogix, or one of these other names? I can't… I'm so sorry.
Alright, I'm gonna follow up so I don't look like an idiot for 20 minutes in front of… one of these has a processor, like in, … one of these processors is, like, a database span processor that's specific to this vendor.
you know, and I don't… you may want to, like.
Do your own research there around, like, how comfortable you are as organizations, like…
whatever, taking… I don't know, I think it's all Apache too, but, like, I don't know how that works. …
They have an implementation of, this…
Similar functionality, that was, like, a…
a draft PR, and then they kept, like, not…
doing the updates, but there is, like, a, … somewhere in here is a PR with an implementation like this. It wasn't reviewed for performance over merged, so that may be… it wouldn't surprise me if Ariel is referring to that and saying, like, he's just packaging his own processor or something. I don't… I can't….
**Kayla Reopelle** 35:29 I dropped a link in the chat to the one that he referred to. It's called the redaction processor.
**Eric Mustin** 35:41 Man, is this new?
**Kayla Reopelle** 35:43 It might be. I think he….
**Eric Mustin** 35:45 Oh, cool. Man, I'm so washed up. Cool.
Yeah, this looks pretty… oh, I guess I'm not sharing my screen.
Yeah, it does appear to have a sanitization… thingy? … Option?
Oh, sorry, I can share again.
Yeah, so they added, if you notice, they added a sanitization capability, A few weeks back…
From this nice person, dude. … Granada.
Okay.
… I wonder… okay, cool. So yeah, it'd be interesting to understand what the…
Whether these, like, options can, in conjunction, be used to achieve this …
The requirements of the span attribute, and like…
It would be… I would love to, like, save everyone trouble and be like, here's an implementation, but, like, we recommend you do this here, or something like that.
**Kayla Reopelle** 36:52 … Yeah.
**Eric Mustin** 36:55 Okay, I don't know.
**Kayla Reopelle** 36:58 Yeah.
**Eric Mustin** 36:59 There's pro… there's plenty of prior art now, I guess you can… … Used to, …
go down as many rabbit holes. This looks like, yeah, it looks like a lot of people have been grappling with it, so it is nice to see… it feels like this will bring that issue to a head of multiple people all over the place with different implementations that have some
Specifics of why they're better or worse. Because that would be… yeah, it feels like common functionality that everyone is going to want, so….
**Kayla Reopelle** 37:29 No.
**Eric Mustin** 37:30 Just random post.
**Kayla Reopelle** 37:32 I eventually want to just, like, provide an option in Ruby, but, …
Who knows how we'll configure it in the end, so that maybe people could leverage the collector.
component as well.
Yeah.
**Eric Mustin** 37:47 Yeah, I wish it was almost, like, …
It's… it's a com… you know, I think, not, you know, I don't want to waste time in the meet. I want to give everyone time back. I think there's this long-standing, and you know, Wendy and Arjun, like, you know, we're just… I'm just… just yapping, where the… the…
Duplication of, like, processor… basically, like, processing of… Both spans, and then, like.
trace chunks, or whatever, just as different, you know, what's required. You know, the collector is not required in a setup, but there's sort of, like, this soft requirement for a subset of, like.
Vague functionality, and… yeah, you can't easily plop… take one and drop it in an app, and take stuff out of the app and drop it in the collector, so, like…
I think this is sort of indic… you know, this is just… this is code smell, a little bit of, like, that underlying architectural…
with, … But, ….
**Kayla Reopelle** 38:44 Definitely.
**Eric Mustin** 38:45 I guess it should happen. ….
**Kayla Reopelle** 38:47 I think we had a late add to the contribib agenda. I see something… Apologies, let me….
**Eric Mustin** 38:55 Let me bring back my… I can share again.
**Arjun Rajappa** 39:02 This was the second PR which I raised related to FOSA scans, so this is, you know, I'm not sure about the approval process, how this gets merged in, so I was just, like, Kayla just approved it, and I was, you know, thinking that maybe even the OpenTelemetry Ruby needs this, so I checked and, ….
**Kayla Reopelle** 39:22 Yes.
**Arjun Rajappa** 39:23 The FOSA scans are failing there.
The PR might look, you know, vague, but I verified things. There are some duplicated jump block validations. That's fine for now. I think that's fine. We can at least visualize things, like, what's going on with, …
licensing, as well as dependencies. So, for now, we can just merge it in.
And, you know, start looking at reports first.
So that's the.
**Kayla Reopelle** 39:52 Yes.
**Arjun Rajappa** 39:52 let's start looking at the reports, then we can finalize on what do we want to include, what do we want to exclude. So, that's my thought here. So, and I'll do the same thing for, you know, the…
original OpenTelemeter Ruby SDK as well, and ….
**Kayla Reopelle** 40:12 Beautiful.
**Arjun Rajappa** 40:13 Yeah, so that was one thing I had. I'll do it for the other one as well.
**Kayla Reopelle** 40:19 Thank you so much. Yeah, it was great to see this PR opened, and I ran the script, like, in our Docker, container. I think it was, like, the app.
Compose, yesterday, and it worked wonderfully. There were, like, a few little errors in it, but, you know, it didn't stop anything, so I think it's fine. And it would be great, yeah, to add this to the core repo as well. I think there's an issue for that as well.
But, if not, yeah, then just go ahead and open the PR. I think it will be great to start getting actual results, and…
I believe the, …
you know, the governance committee will also appreciate that, because I think these FOSA scans are part of the journey to stability for the OpenTelemetry project, or I guess graduating for the OpenTelemetry project, to move from being incubating to, like.
Graduated. I don't know if there's another word for it.
Okay, it looks like I just added to this repo, so, … Yeah, so we're… …
Yeah, I'll look out for your pull request there as well.
And I forget why… yeah, we can merge that today.
**Eric Mustin** 41:31 Sorry.
**Kayla Reopelle** 41:32 Alright.
**Eric Mustin** 41:32 ….
**Kayla Reopelle** 41:33 For sure.
**Eric Mustin** 41:34 Yeah, we… I just approved if we need a second approver.
Cool. Yeah, I'd seen this effort going across some of the other languages, so… yeah, it's generally…
I don't know if it's a hard… I don't… I don't know the… I don't know the requirements for OpenTelemetry, generally speaking, to get to graduated, or whether Ruby needs to come along for the ride at all, but it would be nice to, like, meet the same criteria, so yeah.
**Kayla Reopelle** 41:59 Yeah.
Yeah, is there anything else that people wanted to discuss today, or look at together?
**Wendy Smoak** 42:08 I had a question from earlier. Can you explain the developer experience thing? I found… there's a channel called Tag Developer Experience?
Are those the same people, or is it something else?
**Kayla Reopelle** 42:19 …
Let's see, I'm not sure if they're the same people. The Developer Experience SIG is a group, that's focused on, yeah, like, developer experience, basically user experience, people who are taking these APIs and using them in their applications.
And, they do a lot of… I think they're in charge of all the surveys that OpenTelemetry runs.
And it's kind of a place to bounce ideas off of other people. If you're having trouble implementing something, you can get feedback there. If you are, you know, if you don't like how something works, and you're not sure if it makes sense to
bring it to a spec, that's a great place to brainstorm as well. A lot of people who run that SIG are people who you'll find kind of on the conference circuit, who are talking about OpenTelemetry and, usually work in some sort of, like, developer experience roles as well.
Thank you, Eric. That channel. Thanks.
**Wendy Smoak** 43:16 I did not find the right one.
**Kayla Reopelle** 43:17 era.
The….
**Wendy Smoak** 43:20 I just thought I might wander by and ask about the… what were we talking about?
**Kayla Reopelle** 43:24 Oh, yeah. Yeah, that would be great if you're able to do that, Wendy, to kind of move that forward.
**Wendy Smoak** 43:30 And just seeing what people think or say, or…
At least get it out there.
**Kayla Reopelle** 43:36 Yeah, definitely.
**Eric Mustin** 43:39 Yeah, 100%.
**Wendy Smoak** 43:40 And thanks, Sean, for answering my… my… thread about the memory usage?
On metrics. Unfortunately, Prometheus needs cumulative ones, so I can't do Delta. I mean… I, I could…
Make the hotel collector do it, but… Currently, we're… not.
**Eric Mustin** 44:03 Yeah, that sounds reasonable to me, to want to start, you know.
Avoid doing that translation downstream if you.
**Wendy Smoak** 44:08 It's just debugging anything. The less thing… the less things… there's already a bunch of things to figure out how it's getting from point A to point B.
**Eric Mustin** 44:18 Two things as well.
**Wendy Smoak** 44:19 I tried Delta.
With Betsy, but it just… we…
went back and decided that Metrix was…
Good enough, we'll give it a try.
**Kayla Reopelle** 44:32 Thanks.
That reminds me, if we have the brain space to talk about one more thing, there was…
An issue that wanted some feedback.
… I'll… I'll put it, I guess, in the agenda? Do I still have that open? Yeah.
….
**Eric Mustin** 44:53 Sorry.
**Kayla Reopelle** 44:56 And… I can share if you want.
**Eric Mustin** 45:01 Yeah, sorry, I got distracted.
**Kayla Reopelle** 45:04 No breaks, no worries.
….
**Eric Mustin** 45:08 Please, feel free to share.
**Kayla Reopelle** 45:09 Oh, it's just, like, thinking for a moment.
So, this one, …
So, I believe this user opened up a bunch of issues a couple of weeks ago about places where
The messaging conventions are out of date for some of our instrumentation that should adhere to them.
what's interesting about messaging compared to some of the other semantic conventions categories is that it has this environment variable, the SEMConf opt-in one, available, but they…
aren't marked… the conventions aren't marked stable yet, and the SIG is currently disbanded to make them stable, because there just wasn't enough time or engagement, so the date about when they will become stable is very much in flux. …
this PR, you know, was kind of like, hey, let's just replace everything here and start using the stable conventions, but I don't think we can quite do that, just because we should.
**Eric Mustin** 46:11 Yeah.
**Kayla Reopelle** 46:12 I don't want to catch people off guard, there's already this process in place, …
Those ideas are written in the comment. This user has opened up an issue in semantic conventions to try to introduce this idea of
attribute requirement levels of, like, thinking about things to migrate to or deprecate, and they're seeing this as maybe a bridge to help
handle those, semantic conventions groups that, aren't marked as stable yet, and don't really have a clear path to becoming stable, to maybe avoid the long-lived environment variable
scenario. … If you have thoughts about semantic conventions and, like.
how this, environment variable is working or not working, I think this issue… he'd like to have more, like, thoughts and inputs on it. For me, as someone who's not, like, actively using
the code, like, as a vendor rather than, like, an end user, I feel like I don't have a great sense of where the pain points are, and so if anyone has thoughts about this that is a user, I think that could be really helpful to move this along.
But, but yeah, so just wanted to call that out in case other folks aren't a fan of the way the environment variable currently works.
**Eric Mustin** 47:45 I, …
So the only difference in practice with… if we were to kind of do the choreography that we've, you know, that Hannah's
Undertaking with some of these other,
you know, verticals, or whatever, you, is that we don't really have a way to start that, like, 6-month countdown clock thingy? Is that sort of… it just is open, it's just like, here's a bar, and good luck.
**Kayla Reopelle** 48:11 Yep, exactly. And so….
**Eric Mustin** 48:13 Okay.
**Kayla Reopelle** 48:13 You can just leave the triplicate.
you know, modules there for a long time, for an unending period of time, but I don't know… yeah, I don't know if that's the right choice. I think, you know.
we've already had one PR, that has been submitted to make a change to all three parts of the code for Ethon, so, you know, a user
Found our documentation and was able to follow that, so that's promising.
But it is more of a maintenance lift. I think the other side is that these instrumentations haven't changed a whole lot, and so I don't know how much they will change necessarily, you know, by whenever it gets marked as stable. So maybe it's okay, ….
**Eric Mustin** 49:03 I think, …
I think, … yeah, it's a nice… I think it's worth doing. It'd be a good… it's, like, a good…
Isolated chunk of work, too, that's, like, sort of… the implementation's already out there, just the effort to kind of wrap it correctly, …
Might see if I….
**Kayla Reopelle** 49:19 Yeah.
**Eric Mustin** 49:19 in time. But yeah, probably, I don't want to have it assigned. But yeah, that, I mean, I don't…
… Especially given that some of these gems, yeah, are not… they're not….
**Kayla Reopelle** 49:32 Whatever, not shipping new, major versions, constantly.
**Eric Mustin** 49:36 Probably practice be fine. … yeah, I guess somebody can…
until we have a real PR that is showing the level of effort and maintenance, it's hard to say, like, don't do it. …
Yeah. So, yeah, it sounds, …
Sounds reasonable to me, I don't… I just don't know if I have availability to pick it up, ….
**Kayla Reopelle** 50:00 Yeah.
**Eric Mustin** 50:00 I don't know, whatever is weird sem… sorry, I'm not… I'm, … It's recorded. … whatever that…
effort is. I… I don't think we should wait on that, just knowing how long that sort of process takes, so…
Good to see he's think… the implementer's thinking big, and I wish him way more than luck.
**Kayla Reopelle** 50:23 Yes, yeah.
Okay, maybe that's a good… a good follow-up, then, is…
Curious to see where this goes, but don't necessarily want to hold this back if you're comfortable with adding the three.
**Eric Mustin** 50:39 Yeah, I'll see if I have, see if I have, like, a day I can set aside or something in the afternoon. ….
**Kayla Reopelle** 50:45 Okay. Nice. Do you want me to wait to respond then, until you have a chance to look at it?
**Eric Mustin** 50:49 Yeah, if you don't, if you don't mind, actually.
**Kayla Reopelle** 50:51 Nope, fine, yeah.
**Eric Mustin** 50:53 … Okay, ….
**Kayla Reopelle** 50:56 Thank you.
**Eric Mustin** 50:57 Thank you all.
Everyone's doing great. Thanks, everyone.
**Kayla Reopelle** 51:03 Cool. Thanks for letting me just run, run over everything.
**Eric Mustin** 51:09 What a rip. No, it's great. You're… you….
**Kayla Reopelle** 51:11 J.
**Eric Mustin** 51:12 Well, generally, when you do all the work, you get to talk about it, so… It's never stopped me before, but for most people…
That's the… so it's… it's awesome to see, yeah, you contributing your time and effort here. I certainly appreciate it a lot. …
I might, I might have something next week or something to share, …
I'm trying to feature some hotel room stuff and, like, whatever, my job.
more. So, yeah, I might have something to share. I'm talking to, like, the DevRel people about…
Trying to show off some cool stuff we've done. But, anyway, nothing, nothing for now.
**Kayla Reopelle** 51:47 Okay, cool. That's exciting.
Alright, last call. Anybody else want to talk about anything today?
Okay, I'll take that as a no. Thanks everyone for coming, and yeah, reach out on Slack or GitHub if you need anything until next week.
**Wendy Smoak** 52:07 Thanks.
**Eric Mustin** 52:09 Cheers all. Thank you all.
**Arjun Rajappa** 52:11 Thank you, baby.
