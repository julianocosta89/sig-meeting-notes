SIG: OpenTelemetry PHP SIG
Date: 2026-09-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Bob Strecansky** 03:24 Hey, Chris.
Can you hear me okay?
**Chris Lightfoot-Wild** 03:38 Oh, come now. Hello?
**Bob Strecansky** 03:41 Hey, how are ya?
**Chris Lightfoot-Wild** 03:42 I'm alright, thanks, yeah, how are you?
**Bob Strecansky** 03:45 Just sitting in some gridlock.
Welcome to… welcome to living in Atlanta, Georgia. Holy cow, that's gonna take me over an hour to get… 20 kilometers.
What's going on with you? Anything exciting?
**Chris Lightfoot-Wild** 04:08 Not that much, I think.
Sim old, same old.
**Bob Strecansky** 04:13 No news is good news.
**Chris Lightfoot-Wild** 04:17 Yeah.
Is it, unusually heavy traffic for… for the day, or is it just…
**Bob Strecansky** 04:26 Yeah, I don't…
**Chris Lightfoot-Wild** 04:27 Bill?
**Bob Strecansky** 04:27 There must… there must have been some sort of accident or something, because it's way heavier than it usually is.
**Chris Lightfoot-Wild** 04:35 Okay.
**Bob Strecansky** 04:36 You know, it's… it's like, you have one… Highway incident, and it just completely gums up the works for everything.
**Chris Lightfoot-Wild** 04:44 Yeah.
**Bob Strecansky** 04:46 Classic.
Do you… you're fully remote.
**Chris Lightfoot-Wild** 04:55 Yeah, man.
**Bob Strecansky** 04:56 Jealous.
**Chris Lightfoot-Wild** 04:59 Well, I'm going into the office next month.
For a couple of days.
**Bob Strecansky** 05:03 Well, that's nice.
**Chris Lightfoot-Wild** 05:05 Yeah.
I mean, I live 160 hours, 180 miles away, something like that, so…
**Bob Strecansky** 05:13 Dang.
That's pretty far.
**Chris Lightfoot-Wild** 05:16 So it would be a bit of a commute if,
**Bob Strecansky** 05:18 You could say that.
Do you just go in every once in a while and, like, stay for a couple days?
**Chris Lightfoot-Wild** 05:26 Yeah, we've got, like, usually a couple of engineering days a year, so… about April and October-ish, typically, so… I was, on holiday for the last one, so I've not been down for a bit.
But we did, we had, like, an ad hoc team meetup in about March, anyway, so…
**Bob Strecansky** 05:43 Wait, say that again? I missed that. What'd you say?
**Chris Lightfoot-Wild** 05:45 Sorry, I didn't… maybe I didn't convert it into American. I had a vacation in about April, so I missed the last one.
**Bob Strecansky** 05:53 Oh, oh, I see.
**Chris Lightfoot-Wild** 05:54 Ugh.
**Bob Strecansky** 05:57 I didn't convert it into a kid.
Easy translation.
**Chris Lightfoot-Wild** 06:06 Hi, Paul.
**Bob Strecansky** 06:07 It's…
**Pawel Filipczak (Elasticsearch B.V.)** 06:08 Hey.
**Bob Strecansky** 06:09 Whoa!
**Chris Lightfoot-Wild** 06:15 Is it… are we expecting Brett? Yeah, that was its,
**Bob Strecansky** 06:19 One of these days, I would expect him to show back up, but…
**Chris Lightfoot-Wild** 06:23 I see there's a bit of activity, there's, like, some online…
**Bob Strecansky** 06:27 Yeah, they'.
**Chris Lightfoot-Wild** 06:27 the gun, and…
**Bob Strecansky** 06:28 There's some… there's some mutterings, he did a release.
**Chris Lightfoot-Wild** 06:33 Oh, nice, okay, yeah.
**Bob Strecansky** 06:42 Yeah, we can… we can get rolling. I don't expect anybody else to yell.
**Chris Lightfoot-Wild** 06:48 Cool. Do you want me to share my screen if you're,
**Bob Strecansky** 06:52 Yeah, I can't… I obviously can't…
**Chris Lightfoot-Wild** 06:54 Yeah, stick on the road. Yeah.
**Bob Strecansky** 06:56 Yeah, if you want to, that'd be great.
**Chris Lightfoot-Wild** 06:59 secured.
Open up the, dock.
Bye.
Everyone's alright. Open up all the numerous tubs.
**Pawel Filipczak (Elasticsearch B.V.)** 07:38 In the meantime, I just created a pull request for the release, For the distro, it just contains the bumped caro.
instrumentation package, and the release notes, so if you… what… Find some time, please take a look today.
And I was… I will push the dark and trees.
**Chris Lightfoot-Wild** 08:05 Taloo.
Ugh, amazing.
Got a Zoom error.
Going a bit slow.
Can you see that?
Sorry, it popped up saying it crashed, but then it kicked back into life, so I'm safe for now.
So… issues for the day… sorry… Should've done this earlier what we're trying to wear.
Hmm.
Cool, so was that the only thing you wanted to put on the agenda for the day?
Paul, do you have anything else?
**Pawel Filipczak (Elasticsearch B.V.)** 09:29 No, nothing from…
**Chris Lightfoot-Wild** 09:34 I'm just gonna let… Sometime… Well, okay, so yeah, I've just written down there, sorry for your benefit, Bob, I guess, as you're audio only. The packages PR that I merged in, sorry, that you merged in, Brett commented on it, saying.
probably need to add you or Bob, or… and or, I suppose, during the flow.
So I wondered, actually, if… Is this the right… is this the right functionality we wanted anyway? Like, also, he asked… What's his wording?
Yeah, would we ever need those credentials as well?
**Bob Strecansky** 10:39 I don't… I'm not… I'm not sure, like, I feel like if we have the automated flow, that should be fine, but is he… is he worried just about, like, manual intervention, or I'm not sure… what is his concern there, do you know?
**Chris Lightfoot-Wild** 10:51 Well, it looked like… so I did… I tried to look on that account, it did that in that workflow, at least when I run it offline, because there's two points there. When I ran it with, Nectos Act, I think it's called, is that? The, sort of local workflow simulator thing.
It created some of the missing packages.
But then it only adds… The account that you're currently on is the maintainer?
And then it looks like a, sort of, a limitation, shall we say, I guess, of Packagist.
That you're also not a maintainer by default.
So, like… As a maintainer, you kind of own the vendor namespace, and you can add some other… Maintainers to one package, and then they can just create separate packages that you're not then a maintainer for?
So, I guess his concern was if, like.
that account just… we lost access to it, and then you and Brett couldn't… Get into those packages, and tweak them, and delete them, and whatever.
So, I guess it's… We could look into that to add… if you can add on their API, maintainers automatically, which I guess would solve that problem.
And then, the second point you made was the email credentials. Like, I made a new account, and I was going to ask if we've got a means of I guess, putting it somewhere in the OpenTelemetry org, like… Do they have a special email set up, you know, for these accounts that have had to be created?
related to OpenTelemetry stuff.
I obviously don't need access to it, you can just transfer it across there, and… The credentials can live.
Outside of… well, currently my control, I suppose, but I don't need them. I just need the API key.
I don't know if that was one that, like, you were aware of. I couldn't see anything in the community guidelines for it. I mean, maybe it was one to ask Severin?
Or I'm just not looking in the right spots.
**Bob Strecansky** 13:02 Yeah, Severin might… sorry, I was talking on mute. Yeah, Severin might be the right person to ask about that. I'm not sure where we're supposed to put that… those credentials. I think that the onus of that probably comes to the maintainers and the contributors and stuff, so… I'm not 100% sure, but that seems… asking Severn seems like a pretty good next logical step.
**Chris Lightfoot-Wild** 13:22 Cool. Alright, I'll, reach out to Severin, then, his, emotional here.
**Bob Strecansky** 13:27 Yeah, we don't want… we don't want any sort of bust factor there, that's for sure.
**Chris Lightfoot-Wild** 13:32 Yeah.
It looks like, potentially, there's another hotel bot account that I'm guessing must be… for one of, like, maybe Tidal set up, and, years ago.
**Bob Strecansky** 13:43 Yeah, I know that he sent up that OpenTelemetry bot account a long time ago, but he was kind of unclear about setting it up. So, again, the, like, ambiguity of ownership is tough, especially in something where people tend to be more ephemeral.
But what are you gonna do?
**Chris Lightfoot-Wild** 14:02 Sure.
Don't know why I just deleted that.
Did I put that right? Apologies, Severin. What was everyone?
Yeah, thanks for that.
Is there anything else I have on my… my… oh, the, the Zismor thing, sorry, as well, if it's alright, I'll just tack that on as a quick thing that… Should've filled up. Yeah, totally.
**Bob Strecansky** 15:02 Charlie Lloyd, what's up?
**Chris Lightfoot-Wild** 15:03 So, attacked… Trust, in that PR that I've got in Contrib.
And I'll… might as well open it so I've got it as a point of reference.
Somewhere in the seat of PRs.
Yeah, so I asked, for his input on the Zizmo workflow, so I found, obviously, we could suppress, well, renovate from actually constantly updating the tags, but then Zizmo was unhappy with that.
**Bob Strecansky** 15:46 Yeah, what are the other SIGs doing for that, as you look?
Sure, this is.
**Chris Lightfoot-Wild** 15:52 Don't…
**Bob Strecansky** 15:52 of them already. I just haven't come across it yet.
**Chris Lightfoot-Wild** 15:54 Well, no one else is kind of doing the same thing we're doing here? Like, the workflow self-referencing.
And then obviously doing a git split, So he said it's… he thinks it's justifiable from a security perspective, given it's part in our own repository, rather than an external one.
And especially given that they are, currently read-only and don't receive secrets, so you seem kind of okay with that. Yeah.
**Bob Strecansky** 16:24 is reasonable.
**Chris Lightfoot-Wild** 16:25 He said one alternative would be to create a long-lived branch, specifically for those workflows, and the callers could remain pinned to that branch's full SHAR.
And then Renovate could just update those when the branch updates.
Which I did say was a similar thing, I guess I was using, in my head, it would have been a tag, but you just, you know, update the tag.
But… So we could either go that route, but the only thing then is, obviously.
if you were to change something in a PR, the like, head.
it wouldn't… it wouldn't reference itself. So, like, another contributor has opened a PR with a change in it.
And the workflow… is referencing Maine, or whatever the head of that branch would be.
But… I guess, is that preferred for security, or what would the…
**Bob Strecansky** 17:24 Yeah, I'm not… I'm not 100%… I'm not 100% sure. I know that usually it's some… it's… they've been really adamant about pinning specific SHAs rather than using head or main, but… If that's our only option, then that's what we gotta do, but I think, I think… Yeah, I'm not… I'm not 100% sure. Maybe, yeah, that might be a good thing to ask in either… either in the hotel admins channel, or in the maintainer's channel, see what other… SIGs have… how other SIGs have solved this problem.
**Chris Lightfoot-Wild** 17:57 I mean, do you think it's potentially a problem viral making, I suppose, though?
**Bob Strecansky** 18:01 I mean, I guess… I'm pretty sure none of the… actually, that's true. I'm pretty sure none of the other SIGs are doing the git split thing, and our workflow might be atypical.
**Chris Lightfoot-Wild** 18:11 Yeah, so we're kind of maybe rightly or wrongly, breaking new ground. He sort of suggests that he was okay from… initially from this, and this one seems like the one with… probably the least foreseen problems, but, there's always, like, what-ifs, isn't there? I suppose.
So, do we, between us, have a consensus of, like, a preference to any of these things? Have you got any opinion, Pawel?
**Pawel Filipczak (Elasticsearch B.V.)** 18:40 No, it's really…
**Bob Strecansky** 18:42 Yeah, I have no… I have no real strong preference, whatever. I think… Whatever is easiest for now is the best, and then if we need to make changes later to meet a security policy or something, that's fine too, but…
**Chris Lightfoot-Wild** 18:56 I think… I like telling Zizmo that these things are kind of an okay thing for now, because of our setup, I think was my preference. And then, just for the ease of development, because obviously you can make a change in the workflow in the branch, et cetera, and just not have to worry about where that comes from.
And then down the line, if it's, like, really a problem, we have to pin these things.
potentially splitting the workflow out into a separate repo. Obviously we can just do PRs against that, and, like, the usual workflows could work as well.
Just because branching off of… so if you had, like, a separate branch with Contrib, and only ever updated it when you were wanting to change the workflow, the other files that exist in Contrib as well are still in the tree, and it just… You know, it would end up looking a bit confusing if it was trying to reach out Of its own, like… Workflow directory, or just… it seems to… I don't know, it seems like there'd be a bit of danger there.
**Bob Strecansky** 19:56 Yeah.
**Chris Lightfoot-Wild** 19:56 Might be worrying over nothing, but…
**Bob Strecansky** 19:58 Yeah, I think… To me, we cross that bridge when we get there, I don't think we have to worry a ton about that right now, but… Do you have… do you feel differently?
I don't know.
**Chris Lightfoot-Wild** 20:08 Nope.
**Bob Strecansky** 20:09 What's your biggest… like, what's your biggest worry in that case? Maybe I'm just not understanding completely?
**Chris Lightfoot-Wild** 20:17 Well, and it… He'd have a downer branch, so…
**Bob Strecansky** 20:21 Yeah.
**Chris Lightfoot-Wild** 20:24 Not that it's, like, a huge worry, but, like, there's a PR as an example that I'm just gonna, you know, go back to. Someone's changed the extensions that they wanted to run for their particular workflow.
But in their PR, you… you couldn't… you couldn't pass and then merge that in, because they would have to either have the PR with a reference to some other… their own fork on it, with whatever branch.
And then you'd say, yes, that's fine, but now please admit it so it'll work in men.
Or we just… Don't have to have that sort of circus of events, and just keep with the branch you're on.
Being what runs the changes.
And then, I guess, ideally, like, if we were gonna say you have to tag a dependency.
Would split just the workflows out into their own repository, and openTelemetry PHP org.
And, you know, have full control of that, and it would be a very small set of… Files, but very specific tags that we can create, Rather than the branch thing, but… Maybe that might not be a strong example. I don't know if I've just justified or helped anything there.
**Bob Strecansky** 21:40 Yeah, I'm… I think the right answer is I'm not 100% sure, and I don't want to guide you the wrong way, because I don't actually know myself.
**Chris Lightfoot-Wild** 21:51 I could try it one way, and then if we get told it's not ideal, then we can change it, I suppose.
**Bob Strecansky** 21:56 That's how I feel, too, like… I think we just have to go with… Like, we just have to come up with the best solution that we can right now, and then if we have to change it later, that's fine, but…
**Chris Lightfoot-Wild** 22:07 Cool. Yeah, I mean, if we can get a bit closer to green, which is, I guess, what Pawel's been doing as a…
**Bob Strecansky** 22:13 Yeah, I feel like that's it.
**Chris Lightfoot-Wild** 22:14 anywhere.
**Bob Strecansky** 22:15 That's imminent, so…
**Chris Lightfoot-Wild** 22:17 Cool. Alright, well, thank you for that.
**Bob Strecansky** 22:20 Yeah, thanks for… thank you for driving that, Chris. I know that that's… like, very classic tankless work, so I appreciate that.
**Chris Lightfoot-Wild** 22:28 Oh, I'm good. Cool. So if there's nothing else on there, I guess we can quickly walk through the board, and you can, listen, listen through, what we're seeing. Yeah. So looking at the issues on the… The main repo.
Neva has raised one.
Which is about missing implementation for attribute count limit and attribute value length limit.
I guess it's just opened as a… potentially a help-wanted kind of thing. I did have a brief look at, like, another SIG to see what they were doing, with that, I think it was the Go one.
I've not got time at the second to do it, I don't know if we just stick a help-wanted label on it for now. If we do get time, obviously, have a look, but…
**Bob Strecansky** 23:15 You could put that… you could, I really like the help label… the Help Wanted label, and I think we gotta… I don't know about you, but I think we gotta get in a better practice of… actually putting things on the board so that it just becomes more rel… like, the board becomes more relevant. I know we've talked about that before, but if you can just put it on our, active back… you know, whatever that active backlog board is.
**Chris Lightfoot-Wild** 23:36 I'll put it on the board right now. There you go.
**Bob Strecansky** 23:38 dear.
**Chris Lightfoot-Wild** 23:42 Cool, this is a… Do we have a… There we go, put it in to-do, and see if… Maybe I should have opened the board as well as a separate, so… I'll come back to that.
Oh, another one from Nuvi as well, so that probably needs to go onto the board. Metrics exemplar filter, does not accept the specification values.
I'll do the same, if that's alright. Help wanted, and stick it on the board, just in case anyone else decides to jump in, otherwise we can… Yeah, understood.
**Bob Strecansky** 24:23 I feel like that's a workflow we have to continue pushing on.
**Chris Lightfoot-Wild** 24:27 Yeah.
**Bob Strecansky** 24:30 I feel like it's one of those things, like, it's inconvenient, but then once you… like, once we get doing it consistently, then it will be… it will become easier.
I'm a flexed muscle, as they say.
**Chris Lightfoot-Wild** 24:43 Absolutely.
So there's a… one as well for Falcon PHP framework, instrumentation.
**Bob Strecansky** 24:53 Yeah, that's… I… I understand, like, I love to hear… I love to see that we're getting these sort of things in our SIG and that kind of stuff, but, like, that can't be our focus. If somebody wants to implement Falcon PHP support, that's fine with me, but I don't want to actively do it, so… A great helpline for the situation.
**Chris Lightfoot-Wild** 25:14 Well, the, the person's, I guess, just been following the, open the issue on the board kind of approach, and… Got it. To the issue and the implementation.
On the same day. So, I guess they had a mind that they need to do this.
**Bob Strecansky** 25:27 already.
They did it already. Well, even better.
**Chris Lightfoot-Wild** 25:31 Yeah, myself and Brett have, started, sort of reviewing that, so that one's kind of… in process. Now, the only… the only thing I've got on this one is it… I'm not complaining, sorry, it looks like there's been AI involved here, Which… which is, I guess, fine. But is this person, like, the first one that's ever come and asked for Falcon?
And will it be, like, a drive-by submission?
But… Or will there be a component owner who… Like, could they maintain this themselves, potentially?
**Bob Strecansky** 26:05 That's a really great question, and I think it's something that we're gonna have to deal with more often, and I don't… you know, I don't think I have a good answer.
Because, you know… the worst thing… I'm trying to think, like, what's the best case scenario here, and what's the worst? The best case scenario is this person implements this work.
They use it effectively themselves, other people use it, that's good.
But then, the worst case scenario is this person implements this thing.
And then it's, you know, it's… it's AI slop… it's AI slopped up, and then people… then it doesn't get, It doesn't get the love that it needs. You know, then that's really tricky.
At all.
**Chris Lightfoot-Wild** 26:46 Perfect.
**Bob Strecansky** 26:47 But anyway…
**Chris Lightfoot-Wild** 26:48 Sorry.
**Bob Strecansky** 26:49 I was gonna say, we have to be… I feel like we have to be conscientious of that, but we can't… we can't have AI use as a barrier to entry, if that makes sense, but we can't also just, like.
Accept everything at face value, which is tough.
**Chris Lightfoot-Wild** 27:04 Yeah, well, I did actually see in… so I did that, I put it in Contrib first, I know we did that earlier today, so I'll follow up with the other PR templates for the other repos, sorry. But in looking at the other repositories under OpenTelemetry to see what their kind of wording was.
I mean, they're not all, you know, the… I settled on one from, like, Java and something else combined, but one of them suggests that I'm a human, this is my first Like, contribution, and, like, the first few that come in are, like, maybe minimal Like, but handwritten?
So you can kind of get a grasp.
Whereas, obviously, this is… again, if this is all done and it works, then great, we don't want to bat it away, but equally, if, like, that person's got no desire to help again in future, then it'll just go, sort of, stagnant, potentially, or, you know, bugs will just be there and, sort of, it'll kind of rot away.
**Bob Strecansky** 27:59 So I will… I'm gonna play devil's advocate for a second, because I think we need one, and I think there, you know, there is that… there is 100% value in… an AI-submitted thing, especially for stuff like this, because there's definitely people that are interested in solving this, but don't have the time or resources or interest in learning all the pieces, and that's where we get really… that's where it gets really dangerous to me, right? Like, people want these things, but they don't necessarily know how to write them or maintain them.
So, I agree with you, like, we have to be conscientious of who's submitting.
what's going on, but I also… I mean, Agentic workflows are, like, are becoming very, very prevalent in a lot of companies. I don't… That's so tricky to me, because I don't necessarily think we should exclude people from contributing if they AI only contribute, but I think that just makes our job more difficult.
**Chris Lightfoot-Wild** 28:51 Yep.
Well, that's fair, and I think one of the other things I said, I was thinking, sorry, was that it looks like some of the other bigger SIGs, so, like, the Go, SIG, I guess that's the collector and Collector Contrib.
There's, like, a lot of packages in that, it's obviously a bit of a hotspot, And it looks like they've obviously got a process where… Over a certain period without maintainers, or component owners, that thing is sort of eradicated.
They've got a process over, you know, several months, but they do remove components if it's gone stagnant, or it's, you know, in an unmaintained state.
**Bob Strecansky** 29:34 Yeah, I wonder… I wonder how much that could be, like.
for lack of a better word, roboted, right? Like, if a particular… a particular package in Contrib doesn't see any activity in 6 months or a year.
Then you have, like, some sort of deprecation warning, not only for the people that are actively maintaining it, but also for… just in general, you know?
**Chris Lightfoot-Wild** 29:59 Yeah.
Thank you.
**Pawel Filipczak (Elasticsearch B.V.)** 30:03 Sorry, for interrupting. So, I think if it became stable, then we don't have to, you know, make it deprecated over time, but if it's not a stable version, I mean, it's zero something, then we can, of course, introduce some time.
And then deprecate it after some time. But if it will get into the sib, then… There's no… I think we should not deprecate things.
Over time, because they are stable. But anyway, I think we should ask him at least to add himself to the README, that he's the outer of that, or maintainer, or coat opener, or whatever.
Because in other cases, if someone will… if there will be some bugs, issues, reports, then we… at least we know To whom we should reach out to.
Because now we have to go into the code blame and try to find the outer, or at least we can introduce something like that on the beginning. I mean, I noticed that in the contract repository in Java, there are, let's say, outers or maintainers mentioned in the reading files of the components.
**Bob Strecansky** 31:11 Sure.
**Chris Lightfoot-Wild** 31:15 So they've got, well, they put that in the README as well, you're saying, sorry.
**Pawel Filipczak (Elasticsearch B.V.)** 31:20 No.
**Chris Lightfoot-Wild** 31:22 Maybe that was the Paul First choice that I clicked on.
conferred to Spanish as one of your colleagues, potentially.
**Pawel Filipczak (Elasticsearch B.V.)** 31:32 Yeah, they should be mentioned there. I'm pretty sure that they are somewhere in the bottom.
**Chris Lightfoot-Wild** 31:38 Alright, yeah.
And that's, I guess, something we don't do, is that we… it's only exposed via the component owner's file, which is kind of buried away.
Who's that?
That seems like it's a sensible thing to, sort of, document as well, in the READMEs.
True.
Yeah, if we're in agreement, I guess we can just move forward with doing that.
So, Bob, just because, obviously, you're not seeing the… On the screen here, there's just the README for the actual, you know, the landing page of the component.
It's just documented who the component owners are, and sort of a link to their GitHub profile, etc.
**Bob Strecansky** 32:20 Yeah.
**Chris Lightfoot-Wild** 32:21 And then a convenience link that says, if you're interested in component owners, and then it links into that to show you, I guess, what that actually does.
**Bob Strecansky** 32:30 Makes sense.
**Pawel Filipczak (Elasticsearch B.V.)** 32:34 And if you will mention by name, I mean the outdoors, by name in the ring, then it will be also available in the Git split, right? If it will be splitted, then… the owner will be in the git split, and also in the packages. The actual real maintainer is someone, right? But now, in the packages, the Bob or Brett are maintainers, or Eucharist.
on the, on the, on the panel in packages, right? So there is no real maintainer there of the package, but one of… one of you.
And if you'll add it into the README, then at least someone who has some troubles, problems, then can reach out somehow to the, to the, to the author, or maintainer, owner.
Someone with the knowledge.
**Chris Lightfoot-Wild** 33:21 Yeah, yeah, we could, we could do that, and I guess, maybe it's a… again, like you were saying earlier, Bob, a problem for further down the road when we decide that we've got some, stylish-looking components, like non-stable ones. Obviously, if it's just stable and we're just getting the renovate PRs coming in.
Like, you know, maintaining dependencies, then that's probably different to something that's just… wonky, Obviously, it does add additional noise as well, though, if these people… any number of contributors just come along and say, here's the body of work, and then we're the ones just following up on the numerous renovate PRs that are tagged to that as well.
I guess it's how confident we are with those, relevant PRs coming in, and just… Merging habitually, maybe that's not a problem.
**Bob Strecansky** 34:10 Yeah.
**Chris Lightfoot-Wild** 34:12 But we're just looking at, like… I mean, the Java board's got 12… on the contrary, 12 open PRs, and we've got… Was it, 25?
So we've got a smaller SIG, but if there's… the more and more renovated ones we get in, it's just all the additional overhead.
**Bob Strecansky** 34:30 Yeah, they just become noisy. I'm excited for our… once CI turns green, I almost want to get to the point where if those renovate PRs pass CI, we just merge them.
Because we're… we're doing releases on our… like, the… merging them shouldn't be… it shouldn't ever be a… Why should I say that right? Merging should never be an event.
But currently it is, because we don't really know whether or not things are hunky-dory.
**Chris Lightfoot-Wild** 34:58 You mean we're sort of trying to get toward that, like, CICD, rather than just the CI bit.
**Bob Strecansky** 35:04 Yeah, exactly. That's my… that's my two cents. Do you feel differently?
**Chris Lightfoot-Wild** 35:09 Yeah, nice. That'd be nice to… yeah.
have more regular releases, and I think at the moment, like I said, people are chasing up, they're like, hey, this thing landed weeks ago.
**Bob Strecansky** 35:19 Yeah, yeah, yeah.
**Chris Lightfoot-Wild** 35:20 I'm wondering if you're gonna release it, or, you know, it's a whole extra thing for us to do.
**Bob Strecansky** 35:26 Yeah, and the more often we can release, the less chance we have of catastrophe.
**Chris Lightfoot-Wild** 35:32 Dear.
Nice, okay, any other PR? Sounds good.
Jump forward a bit that, Okay, well, I'll, continue on with reviewing that one as well. We can add those comments, like, to the component owners to see if the author's potentially interested in that.
I mean, I guess if they say no, we can sort of accept it and see if anyone else That would have otherwise been interested in that, you know, component would step up or try it, and… Never know who comes out of the woodwork, I suppose.
There are a few other, issues, but they're sort of weeks old at this point, so you can probably just look into those, outside of this call.
I think some people have already… I seem to recall Nive commenting on this one, I think… yeah, the author's responded to it, and I don't know if that counts as, like, resolved at that point, that, like, this is… this is fine, Maybe we need, at some point, to go through these… this issue board, and maybe triage them a bit better than we have been.
**Bob Strecansky** 36:41 Yeah, maybe we can do that next week. We can, like, be explicit, saying next week is just an issue board cleanup day.
**Chris Lightfoot-Wild** 36:49 Yeah, that sounds good.
**Bob Strecansky** 36:50 If y'all are good with that. I think I agree with you, Chris, we're desperately overdue for an issue board cleaned up.
**Chris Lightfoot-Wild** 36:58 Yeah, sounds good.
Oh, I think I've closed the contrary tab by mistake at some point, but I'll come back to it. Distro, Pawley said you've got one already there, this 9.7 release, I'll open another tab and come back to that, later.
That's fine.
You're having fun with Renovate as well, I see.
**Pawel Filipczak (Elasticsearch B.V.)** 37:25 Yeah, I have to review that.
**Chris Lightfoot-Wild** 37:27 What's that… this, the workflow, the shared workflow, is that something that you're on with as I can, or does that give you any problems?
**Pawel Filipczak (Elasticsearch B.V.)** 37:39 So I wasn't even, you know, analyzing what's… what is it about, and I should do here, so… Don't have time to review that.
I guess it's… Alright, simplified now. Okay, I'm good.
So, yeah, it should be approved.
**Chris Lightfoot-Wild** 37:58 Nice. I did the one in Contraberg a couple of weeks ago, and it's not seemingly broken anything, so… if that… if that counts… if that gives you any confidence or not, who knows?
Other than that, there was nothing else you needed, you just let me in.
Release prep one.
Cool.
Instrumentation repo, Renovate a shared workflow again, which is probably… So, it's only yourself, Bob, and Brett at the moment that can merge on these, so I typically… not really having any C expertise myself, don't tend to look at these.
**Bob Strecansky** 38:43 Yeah, feel free to… can you just cop… Just DM me that link, and I'll take a look at it?
**Chris Lightfoot-Wild** 38:49 Yep.
Oh.
tag you as well, I'll send you a link after this, call.
**Bob Strecansky** 39:00 Thank you.
**Chris Lightfoot-Wild** 39:01 And then, sorry, I said to come trip… Yeah, up to 32 PRs, could probably do with a bit of a… Go through that as well.
Yeah, I'll try and get some time in to do some of those. It's been a bit busy recently, so, Trying our best.
Cool. Was there anything else? We've… I think we've gone through all the bulbs there,
**Bob Strecansky** 39:33 Oh, good for myself.
**Chris Lightfoot-Wild** 39:36 Cool, alright, thanks very much.
See you next time.
**Pawel Filipczak (Elasticsearch B.V.)** 39:41 You guys, thank you. Bye.
