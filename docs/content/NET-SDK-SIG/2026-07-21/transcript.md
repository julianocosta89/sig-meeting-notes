SIG: .NET SDK SIG
Date: 2026-07-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:51 Pete.
**Alan** 01:52 Hey, Martin.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:54 How's it going?
**Alan** 01:55 Not too shabby. How are you?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:58 Yeah, not about… it's cooled down a lot here, so…
**Alan** 02:01 Very good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:02 Gutt.
**Alan** 02:04 That's much better. It's warmed up here. Maybe not as hot as it was where you are, but yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:11 I didn't realize you were on holiday last week.
**Alan** 02:15 Oh, oh, I wasn't. It was just out on Friday, so I just…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:19 Okay.
**Alan** 02:22 And I'll actually be out this Friday as well.
But nope.
I'm around.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:33 I thought maybe you'd caught the sun a vacation bug.
**Alan** 02:37 Yeah, I know, that seems to be going around, right?
the whole .NET SIG should just take a vacation together or something.
Seriously.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:48 get, budget for it from the foundation.
**Alan** 02:52 Yes.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:55 Hey, man.
**Alan** 02:56 If you're gonna make that happen.
Oh, hey, Matt.
**Matthew Hensley** 03:07 Hello.
Simiola… Got the same fun login prompt to join the call.
**Alan** 03:15 Yeah, new process.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:18 I didn't, but maybe I absentmindedly accidentally clicked on the link previous to today.
So I've already done it.
**Alan** 03:31 Yeah, there was an option to, like, log in with a Linux Foundation account.
Which I think I might have, but… I don't know the password to it.
I don't know where that gets you.
If you log in via the account versus just as a guest.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:52 Yes.
**Alan** 03:52 learned.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:54 It, I guess, being that can ask Meridia?
She's in the GC, she should know.
**Alan** 03:59 Yeah, yeah, yeah, yeah.
Yeah, I think based off of what she was describing last week was… There's still some… Kinks to work out as far as, like, control over the Zoom calls, so maybe, like, if we're a maintainer and we need to, like.
boot somebody or something like that. You probably have to be logged in to be able to have those permissions to control the meeting.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:27 Yeah, possibly.
Yeah, we have a weekly team meeting tomorrow, so we can ask her what the incantations are.
**Alan** 04:36 Yeah, cool.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:39 There was nothing in the agenda, so I figured we could try and use the new dashboard.
**Alan** 04:46 Oh yeah, sweet!
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:48 So, yeah, I didn't realize when Meridia explained this, or I didn't pay attention, which you did, that the pull request goes in the shared workflows repo, not in our own repo. So there wasn't actually anything to change on our end.
So now there's this issue, and it's… as long as GitHub isn't having a wobbly in actions.
It seems to keep up to date.
any group.
It looks like the way it works is it groups everything by, sort of.
tier… I wouldn't say urgency, but, like, tiers of… The stuff you could probably action quickest is at the top.
And then it worked fine, so… For the main repo.
There's… so it's got, like, waiting on maintainers.
So this one, it's got lots of ticks, but Raj, put a comment on this one.
Asking to hold it for now, to possibly revisit it.
But that's not apparent on here. And then I think everything else, it's sorted by the last time the PR was touched.
**Alan** 06:03 Nice, yeah, I still owe a review on… at least one of those PRs from Steve.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:13 Hmm.
**Alan** 06:13 The… what was it, the configuration-related one?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:17 Oh, yeah, that's on a… yeah, that's the contrary one.
**Alan** 06:21 Oh, yeah, yeah, yeah, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:25 Just flip back to the main repo a minute. So, there's just a bunch of… not that important PRs. For me, this afternoon I am.
I pointed Claude at the repo again, and it found a few things that I didn't think quite met the bar for, like, having to go through the security process.
But that's what I was telling it to look at, at least.
And it found a few bits and pieces here and there. It's different, it's different today.
These are… these ones are all waiting for whoever opened them to respond to feedback, or fix broken tests, or fix merge conflicts.
And then crafts at the bottom.
So we don't really have to do anything about those, but The other thing that got changed with this as well, I don't know if you saw at the weekend, Trask added a new feature to it to comment on PRs as well.
to, like, keep them in sync, so I'll just pick one of mine, just to demonstrate.
I can't decide if I like it or not, because it's more notification noise, but, it now leaves these comments on the PR that shows, like, what the current status is.
**Alan** 07:44 Oh, interesting, I see.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:46 And there was a flurry of activity on Saturday from it, because it went through every open PR, no matter how old it was.
So there's, like, so as it caught up.
with, like, current state, I got a deluge of notifications from GitHub.
**Alan** 08:03 I see. Yeah, and it also seems like this might be… noisy. Will it continue to put a comment every single time that the status is refreshed?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:13 So, it just does edits…
**Alan** 08:15 So you get… Oh, okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:16 You'll get a single notification the first time it does something, and then it'll just keep it up to date.
But when you, like, when Dependabot… not Dependabot, when Renovate runs.
like, you get a notification that Renovate opened a PR, then you get a notification that CodeCov did the coverage on the PR, then you get this comment from the dashboard bot telling you, hey, there's a PR. It's like, I knew there's a PR.
**Alan** 08:41 Yeah, and then you gotta scroll, like, a mile down to…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:44 Yeah. Actually, so…
**Alan** 08:45 Real comments.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:47 I'll give it another week, but I might consider… doing a PR… well, I mean, it depends on what we want to do collectively, but, to add the option to opt out of the comment?
Yeah. It gets a bit noisy, because, yeah, I don't think the comment was implemented at the point we added the dashboard, so it was just like, oh, cool, an issue.
But now we've got issues and comments.
**Alan** 09:11 Yeah, it seems reasonable to disable it. Though I would, I would be, I guess, somewhat curious about how the value that Trask sees in it, because I know he's… You know, a very active maintainer, and… I wonder if this helps him somehow.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:25 I think, to be fair, when it did the initial deluge, I think a few old PRs, it made the people who'd opened them, like, go, oh yeah, here's a PR I've forgotten about.
**Alan** 09:39 Huh.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:40 But I think they only went as far as, like, you know, making it up-to-date with Maine.
And that was it, rather than actively looking at the comments or anything like that. But it did cause a little bit of activity as, like, a… A non-human poke, as it were.
**Alan** 09:59 Yeah, yeah, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:03 And then it's an trip.
So yeah, so that's the PR from Steve to add in the scaffolding for the dynamic control stuff.
And… where else we go.
I forget which one this one's about, but it is in, he's… Waiting on those two guys, as it's Geneva, and there's conflict site anyway.
then there's a bunch of PRs for me that are mostly, like, trivia.
like, flaky tests and things like that. And then, the one I… the two I messaged you about.
Friday, Alan, or just 911?
I'll open them in a tab, and we'll flick to them in a second. What was the other one?
Oh, fantastic.
Yeah, there's still got the probability… consistent probability sampler, One, and then there's a couple… of extra ones today from my Clawed adventures.
interesting one that it flushed up, but I don't think… again, I don't think it was a security thing, is it flushed that the Lambda instrumentation doesn't do the query string redaction.
Compared to all the other things. So I've opened a PR that adds the ability to do that.
But I guess maybe there's some context somewhere as to why it didn't get done, or if it genuinely got omitted, but I've done it the same way as all the others, where there's an environment variable to opt out.
If necessary.
**Alan** 11:43 Right, yeah, no, it was probably just an oversight, I'd guess.
Actually, somebody had reached out to me.
I think somebody from Peter's team met a little while back, and had asked about… That environment variable, and why we had gated it, and… I told him that I'd… I remembered that there was some history there.
And… I think it had to do with something, like, we were waiting on the spec to… Make a decision with respect.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:19 I see.
**Alan** 12:19 and… And I… the… my brain was foggy, so I… I never… Or maybe I never knew, like, what the end result of that was, but anyways… question, can we remove that environment variable now, I think is… is something that we should, follow up on, see if there's still an outstanding spec thing. I just don't… recall, or I never really followed that issue super closely.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:52 I'll just make a note, and I'll have a look tomorrow.
whether there's something in the specs to follow up on that. I, I know, I know it's definitely now recommended.
That we should do the reduction, so you have to opt out.
But yeah, I don't know if there's, like, a… Designated control mechanism that you should have a way to opt out of it, out of it.
**Alan** 13:15 Yeah, oh, interesting. Well, so yeah, then that… that does seem different than… from what our current behavior is, right? If the spec does say, This should be the default.
Then we should…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:29 Yeah, when I looked at it, I checked it today, before I opened the PR, and it says something along the lines of, if you can parse the query to know what the parameters are, then you should redact it.
And we've already got, like, a shared helper code to do it, so… it was… most of the change for Lambda was just wiring it up.
**Alan** 13:56 Yeah, gotcha.
Yeah, I think, I think people's… Interpretation of should.
Sometimes… varies.
It has normally been.
It's required.
Unless there's, like, a really good reason That you can cite where, like, it's impossible, or something like that, or…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:19 Yeah, I think the way I usually parse it is, if it's written in normal English.
Then it's, like, a very strong suggestion.
But when it's all caps, spec, should… It's sort of a like, we'd really like you to, but you don't have to.
**Alan** 14:36 Yeah, yeah, it's just, I think, a slightly different, you know, I don't know which interpretation is valid, but I consider that interpretation a little bit different from mine.
like…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:46 Okay.
**Alan** 14:48 Like, but I just think of it as, like, it's basically a must.
But it's only a should because there might be some, like, edge case where, like.
Doing it is not possible, or something.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:01 Yeah, I think in my brain, it gets a bit fuzzy, because we also have recommended And it's sort of, like… Which one's which?
**Alan** 15:11 Yeah, yeah.
Anyways… Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:18 Yeah, so there's a few extra ones on the list.
now, from today, but, none of them are urgent. These two are the ones I messaged you about on Friday, so schema URL, that's a new feature that's in 1.17 of the SDK.
So, I figured it just made sense to ship the 117s.
Of the resource, detectors, with the support to use it at the same time.
Rather than do the 117s.
And then have a follow-up.
It looks bigger than it is, because… when I was doing… updating the .NET 11 branch this week, they added a new type in the latest preview called Activity Source Factory.
which is the exact same name as the type that I added a few months ago, called Activity Source Factory, and it caused a load of compilation errors. So I've cherry-picked through a bunch of tweaks to, like, Hadeus.
it, so it doesn't cause those problems. So it looks like it's touched loads of stuff, but it's… Most of the files touch the one-liners.
But… and then… Because… that PR then meant that I was emitting a schema URL, when Copilot… what was it called? When one of the… I got an agent to, like, review the PR, it found a few edge cases in the semantic convention compliance So then there's a few add-on commits that fix those bugs, because I figured it made sense to just roll them up into this.
Rather than split out into, like.
four PRs, one type of schema URLs, and then one each fruit of the bugs.
**Alan** 17:15 Okay.
Seems reasonable.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:19 But yeah, they're nothing struttering, it was like, you know, OS type should be lowercase.
one of the GKE… Attribute names have the wrong name.
And a time wasn't being UTC-fired.
**Alan** 17:38 Oh, interesting. Fixed cloud zone. Should be cloud availability zone. Is that a, I'm not super concerned, but is that technically a breaking change?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:48 Someone can… someone can check and find if I'm mistaken, but when I looked into it, it appeared that it had always been called that, and I think it was just a mistake.
I couldn't find any evidence of it being renamed at any point.
**Alan** 18:04 Okay.
So yeah, then we could just consider it a bug, basically.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:10 Yeah, yeah, unless there's something in the semantic conventions repo I missed in the change history somewhere, and it was an intentional change, but I couldn't find Cloud Zone in there anywhere.
**Alan** 18:22 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:25 And yeah, that's pretty much it. So, where's the… so… oh yeah, you might not have seen this, Alan. I… a couple of weeks ago, I put in a GitHub Actions workflows runs.
Weekly, but you can run it manually. And it just goes to all the change logs and finds any that have got, like, unreleased stuff in there.
And it just gives you a… this is the stuff that we haven't released all the latest code for yet.
**Alan** 18:55 Oh, that's real handy. That's nice.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:58 Because, yeah, it was when I was trying to keep track of What needed a release?
It was just sort of lots of manual trawling through the repo.
**Alan** 19:07 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:08 It won't find, like, commit drift. If there's, like, you know, like, a refactor in there that's not in the changelog, it won't find those. It doesn't go into that level of detail.
**Alan** 19:17 Gotcha.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:18 But if it's got a user-facing documented change, then it will surface.
**Alan** 19:23 Gotcha. Yeah, and I mean, I think we're pretty good about getting changelogs updated when there's actually, like… I mean, I guess… I guess it would… it would miss some… yeah, I don't know. Everything would have a changelog. Everything that would be relevant to, like… for a release.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:40 Yeah, because we wouldn't necessarily, like, release a refactor.
**Alan** 19:44 Right, right.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:46 But yeah, so the stuff that's still left for… until everything's got a 1.17 is all of the resource detectors.
Because of the schema URL PR.
And then the final change is for these three, which is the AWS ones, is Someone reported a bug.
that I made a mistake in a refactoring a previous release, and accidentally dropped the cloud region attribute.
**Alan** 20:18 Oh, okay, so this…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:20 Yeah.
**Alan** 20:21 He used to admit it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:23 Yeah, because the AWPS ones have got that infrastructure to let you pick the semantic conventions version.
I did some refactoring to put more resource attributes… oh, resource attributes… attributes into the AWS SDK calls, and I accidentally messed up the inheritance hierarchy.
And put an override in the wrong place, and it meant that it disappeared.
**Alan** 20:51 Gotcha, okay. But otherwise, cloud.region was previously present on all of the versions of the AWS instrumentation, based off of that, like, enumeration.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:02 Yeah, so it was… it's in all the previous releases, and then when I added the 1.40 semantic conventions, I introduced a bug that meant that unless you were targeting latest, it disappeared.
And all the tests always only tested latest, which is how it got missed.
**Alan** 21:24 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:26 So… I've fixed it, and the tests now test all of the versions.
**Alan** 21:31 Nice, nice.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:34 But yeah, I figured he might as well hold back the 117 for this fix, rather than, Do 117, and then do a 0.1 to fix… Bug that was already shipped.
**Alan** 21:48 Sure. Okay, yeah, no, both those PRs look pretty… I'll give them a quick glance over, but they're… Sounds good. Sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:57 Yeah, and then whatever's been looked at by tomorrow morning, I'll finish the 117 off.
Because it's just those bits that are left. All the others, I did on… Thursday.
**Alan** 22:13 Yeah, okay, cool.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:17 That's all we got on the dashboard.
**Alan** 22:22 Alright.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:24 Is there anything else you have, or you had, Matt?
**Alan** 22:31 Not from my side.
**Matthew Hensley** 22:34 Not currently.
Just catching up on… A few things, I was double-checking the probability sampler for… some completeness things, so the math gets…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:46 Cool. Fine.
Yeah, I was… I was grateful for wherever it is in the OTEP that there's a big matrix of… here's a load of values, and if you plug them in, here's the probability you should get.
**Matthew Hensley** 23:02 Yeah, I think we know how that one got written.
**Alan** 23:06 Nice. Is it, like, a kind of… almost a test suite type of thing?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:10 Yeah.
**Alan** 23:11 Nice.
Yeah, that's the other PR that I actually owe you a review of, right? You would ask me… I took a note somewhere.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:21 Yeah, yeah, it's just because it's been, hanging around for a couple of weeks.
So, if there's anything I need to address on it, then I can, deep on that, and get it done.
**Alan** 23:32 Cool. Okay.
**Matthew Hensley** 23:35 Just personal opinion on that one, I think that, it's gonna be more about interoperability that burns us, much like OTOP.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:45 Oh, so it gets carried around the system correctly?
**Matthew Hensley** 23:49 Yeah. And does everyone else interpret the parameters in the same way?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:55 Right, yeah.
Yeah, this year, you'll have people going, why doesn't… why isn't this thing the your .NET code sending the sampling to me be my Python app sort of thing?
**Alan** 24:09 I haven't actually dug into it yet, but it uses trace state, right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:12 Yes.
**Alan** 24:14 To pass around its… its stuff.
Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:17 There's, like, a bunch of fun extra parameters to, like, encode, but here's the randomness the last hop used.
Sort of things, so you can theoretically derive the same value.
**Alan** 24:33 Gotcha, yeah.
Yeah, and to your point, Matt, yeah, that's always the struggle. I mean, do y'all have a sense of how many languages have actually implemented this so far?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:46 I really don't, actually.
I didn't look.
**Matthew Hensley** 24:51 There's only a handful. This has been one of those chicken and egg, Hotel things where it can't be stabilized until there's implementations?
**Alan** 25:00 Totally, yeah, yeah, yeah. And people didn't want to…
**Matthew Hensley** 25:04 Oh yeah, good.
**Alan** 25:05 Sorry, sorry. Yeah, I mean, once it actually gets stabilized, once we get enough implementations and they declare it stable, that'll probably be a point in time when, like… People could probably more regularly rely on it being Present across their service boundaries.
And working, but somebody should probably do, like, a cross-language kind of test suite, right?
Like, making sure that all the languages talk to one another right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 25:37 Yeah, that… That makes sense.
**Alan** 25:41 I don't know who's gonna do that, but… It would be,
**Martin Costello (Raintank, Inc. – Grafana Labs)** 25:47 It's a bit like the W3C.
Think that we have.
**Alan** 25:52 Yep, exactly, exactly, yeah.
**Matthew Hensley** 25:56 Well, if you want to target for that, I believe… the Go implementation is the reference one?
So, I think if everything behaves the same.
That one, it is close enough.
Bundalate will require some clarification in the future, because it's floating point handling, so… That's always… Lots of footguns.
**Alan** 26:22 Yeah, totally.
Alright, y'all.
Good talking.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 26:31 See you next week.
**Alan** 26:33 Cool. Talk to you.
**Matthew Hensley** 26:34 consider.
**Alan** 26:35 Right.
