SIG: Communications SIG
Date: 2026-10-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jack Baldry** 00:14 Hello!
**Tiffany Hrabusa** 00:17 Hey, Jack, how are you?
**Jack Baldry** 00:19 I'm very good. I was a bit panicked. I was like, oh.
I only checked the meeting invite. as I was about to join the meeting, and I was like, oh no, it's a different Zoom thing, I have no idea. Do I need to sign up for an account? How late am I going to be? But it was actually quite easy to get in, so that's good.
**Tiffany Hrabusa** 00:35 Yeah, it's an open meeting. So I think we make it pretty, pretty, pretty easy.
**Jack Baldry** 00:42 Hello, hello.
**Tiffany Hrabusa** 00:45 Hi Vivek, how are you?
**Vivek Anandaraman** 00:46 Hello. Good, how are you?
**Tiffany Hrabusa** 00:49 I am good. Thank you. Severin.
**Jack Baldry** 00:54 Oops, I can't hear you.
**Tiffany Hrabusa** 00:55 Good.
**Severin Neumann (Bronto)** 01:01 Now you can hear me. I was muted.
**Tiffany Hrabusa** 01:04 Yeah.
**Severin Neumann (Bronto)** 01:05 Yeah, Cole.
Let me see, we have some things on the agenda. So I need to drop probably around the half hour mark.
But I think maybe we are done by that. So let's see.
So where's my zoom?
I can share my screen if you like.
I'm.
I'm… Can you see that?
**Vivek Anandaraman** 01:34 You see her?
**Jack Baldry** 01:36 user.
**Vivek Anandaraman** 01:36 Yep.
**Severin Neumann (Bronto)** 01:38 or… Should we get started, or should we wait for anybody else?
**Tiffany Hrabusa** 01:49 I don't know if Vitor is planning to join or not.
Maybe give it a minute and see?
Because I know that he would probably want to be here for the chat with Jack.
**Severin Neumann (Bronto)** 02:02 Yeah, yeah, definitely, let's… let's see.
I'm.
**Tiffany Hrabusa** 02:06 In the meantime, I can…
**Vivek Anandaraman** 02:07 even.
**Severin Neumann (Bronto)** 02:07 that the session is recorded so we can, I can then ask every maintainer to… To also follow up on that.
Yep. Yeah.
Okay, we can wait another one or two minutes.
**Jack Baldry** 02:25 is Sorry, I forgot the name of the person we're waiting on, but do they already know the sort of context? Because if we want to make use of that time, I'm… Like, perhaps we just… have a little chat about what it is you're looking to do. I mean, Tiffany gave me some overview, but it's always worth…
**Tiffany Hrabusa** 02:44 Yeah, let's go ahead and get started.
**Severin Neumann (Bronto)** 02:46 Yeah, I think we can get started, and I said, like, this is recorded, so if anybody wants to follow up on whatever we… We talked about, and yeah, they can… they can take a look.
Just give me a… minute… Okay.
**Tiffany Hrabusa** 03:03 So Jack, Severin is another maintainer for OTEL Docs and he's kind of one of the OG maintainers. So.
**Severin Neumann (Bronto)** 03:14 Maybe not OG, but I think right now, one of the longest serving ones.
**Tiffany Hrabusa** 03:20 And so he has the most context for all of the website stuff that's currently in place.
I will just sit back and listen because I don't know.
**Severin Neumann (Bronto)** 03:32 Yeah, yeah.
I can, I can maybe… so… Just to to give you our context, and then again, like like we're super curious to to hear like how you maybe address some of the problems that we have today, or or like so so so the thing is like as you know, like OTEL is a quickly growing project.
We have now around 40 something special interest groups.
Technically, most of them should deliver some content to the OpenTelemetry website.
But of course, for different reasons, there may be, like.
They are doing it, maybe not, maybe they're, like, sending their docs or whatever artifacts they generate to To some other places, and then for the ones that are working with us right now, we recognize more and more how much we are a bottleneck for them to deliver whatever they want to document, right? So for a long, long time, especially, like, when I joined, when OTEL was, like, this was around 21-ish.
Where it was a lot more around, like, hey, nobody knows about OpenTelemetry, so a lot of the docs needs to be really.
explain very well what we're actually doing, and how people can go about it, so we focused a lot on consistent getting started guides across languages, and I think that was mainly the most thing that we had, right? We had the collector and the languages. I know it was mainly it, but now we have, like.
A variety of other tools that landed the documentation, and a lot of other asks that people want to see on our website.
That we've already, for a few years, reached a point where I think, like, that model is no longer sustainable.
And are now looking for, okay, how can we… Make our docs more distributed, more decentralized.
One thing we had at the very beginning Right before I joined, it's like, so initially we had a distributed concept that people had like a website docs in their specific GitHub repository.
And we loaded them as a sub-module into our repository, and by that, like, Build out the documentation.
As you might know, this comes with, like, a variety of its own crappy problems.
**Jack Baldry** 06:08 Yeah, for sure. We actually had our… our CTO, when I joined, Just had very, very strong opinions. I think Git submodules.
is quite a natural way to solve the problem, but is, of course, you know, Kitsub modules are hard to work with.
I think subtrees, if I were to give in a bit more freedom, subtrees are also quite a natural way, which are not an official Git, like, construct.
But, is essentially a similar process, but allows you to more easily contribute back upstream. So one of the constraints we actually have is Organizationally, we have such a… horrible.
aversion to submodules, that we can't explore this more deeply, but I would consider subtrees, and I'm happy to sort of… Okay.
**Severin Neumann (Bronto)** 07:02 I never hear about, like, this was valuable, like, from second one, I never hear about subtrees. So maybe to add that.
Patrice… like, so not sure if you know Patrice, he's from CNCF, he has been, like, with us for, like, since the inception of, like, our website. He's a Doxy maintainer.
And he got the submodules under control really well, so we now have a few workflows that, like, people can run and say, like, hey, npm fix submodules and whatever, and, like, we have a good handle on them.
But with we, I mainly mean, like, people that know what they're doing. So the thing is always, like, with submodules, it's like, if you have a non-technical person, or a non… Jit, a person, then, like, those things can still be really brittle.
**Jack Baldry** 07:58 Yeah, even if you know what you're doing.
**Severin Neumann (Bronto)** 08:00 Yeah, yeah.
So that's already an interesting… is this what you're using right now, or is it…
**Jack Baldry** 08:07 No, so I've not even been able to really justify a proper use of Git subtrees because of the similarity in name to submodules. So, like, getting that to have the momentum internally would be kind of rough.
I guess… So what we are doing is we have a… a job that runs that just has, like, a manifest file that names all of the sources.
And… literally, fetches those… well, clones those repositories and rsyncs, files across. And it's really quite a dumb process. But it does mean that we… one of the constraints we have internally is that all changes need to go via a pull request so that we can run organizational workflows on them. So, it allows us to decouple the, the change from the source repo, and, have it, sort of, make its way through an approved process into our website repo. The big challenge we have is that we now do have a monorepo, which, our technical writers would love to work in exclusively, but… The reverse process is a real pain, like, going from monorepo back to all the source repos.
with what we have right now is not a very efficient or effective process. So, like, and I don't think… From a manifest, works really well.
If you're going in one direction.
The… the reverse… if you're considering allowing people to work both in like a docs monorepo.
**Severin Neumann (Bronto)** 09:49 Okay.
**Jack Baldry** 09:50 Okay, okay.
**Severin Neumann (Bronto)** 09:50 Yeah, yeah, but that's definitely not something… I mean, correct me if I'm wrong, Tiffany, but that's definitely not something we… like, the moment we ask 6 to, like… Whatever we want them to do with their docs, right?
I want to have us spend less cycle on them.
And, do as much as possible, right?
And if someone has, like… More… brings more the technical writing skills to the project.
like Tiffany, for example, has a strong technical writing background, I rather want to see You or anybody work on key pieces of the project, right? That we say, like, hey, focus on the OpenTelemetry collector, or focus on, like, like, I would love to see a few people really, like, work on a A getting started guide that is kind of independent.
of the different SIGs, right? But if the, I don't know, Java, PHP SIG, OTEL injector SIG, whatever SIG says, like, hey, we have our own universe of documentation.
we handle that, and all we do is make sure that it lands on the website. That's, like, more or less my vision, but of course, there's, like, so many moving pieces, like, you called out already, that, like, it's not trivial, right? So, yeah.
**Jack Baldry** 11:20 Yeah, and in our process, because we've we've… Removed ourselves from, like, Git.
plumbing and get actual primitives. We then have to, like, re… Instate metadata as part of the process to help with.
working backwards, I suppose. So, for that, I've been using Git trailers in the commits that come across this with the sync.
**Severin Neumann (Bronto)** 11:47 Lots.
**Jack Baldry** 11:48 source of metadata. But it's It meant that we'd had to build, like, additional tooling to help ourselves in the scenario where something's changed upstream, downstream, I guess, depending on which way you're looking.
And has made it into our monorepo.
So that we can get back to the source and work out what's happened.
**Severin Neumann (Bronto)** 12:07 Because…
**Jack Baldry** 12:08 We… the separate… separate projects, have an ability That… to break the full build.
We… we… are constantly extending the CI that we run in the source repos to minimize that. But, you know, if you think about, like, cross-site linking, that's one of the big challenges that we have. Yeah.
**Severin Neumann (Bronto)** 12:29 Exactly. Like like yeah. Yeah. Yeah. Yeah. Yeah.
**Jack Baldry** 12:32 It's not like a build build failure, but it's certainly a site degradation.
**Tiffany Hrabusa** 12:42 Just… should follow on what Severin said. I don't think that we are that concerned about having bi-directional contributions in this case.
So, I don't think we need to be super concerned about the brittle nature of going from the .io repo back to wherever the docs are living in the SIG repos. Is that right, Severin?
**Severin Neumann (Bronto)** 13:08 Yep.
**Tiffany Hrabusa** 13:09 yeah.
**Jack Baldry** 13:09 Do you have, any… Can… I know you're an open project, but do you have private things like is there some sorts of private docs because that's another dimension that we have as a company that.
**Severin Neumann (Bronto)** 13:22 No, no.
**Jack Baldry** 13:23 Yeah.
**Severin Neumann (Bronto)** 13:24 Everything, like… No, I mean, we have nowadays private repositories within OTEL, but they're not having in any form or fashion impact on our documentation. So our… Let's say, in that case, probably… OTEL is… much less complicated to Grafana, because, like, we are just an open source project, and I said, like, we don't want to have, like, a bi-directional sync.
But what we want is really that thing where we get to a place.
Like, I start to think about docs more like what people are doing in platform engineering right now, right? Where we say, like, hey, we offer you a service, like, this is the thing how you do documentation.
And the SIGs can, like, consume that, and we get out of their way as much as possible, right? And if a SIG says, like, hey, we're a young SIG, or we are small SIG, or we are just out of… ways to do our documentation, then maybe, yes, this would be a situation where I would love to have technical writers focus on.
But right now, we spend so many cycles on everything that nobody can really say, like.
So my wish always for everybody in the SIG, like, let it be myself, or Tiffany, or Vitor, or Patrice, or Vivek, you're here as well, right? I want contributors to this SIG while there's, like, a big chunk of, like, must-dos, right, that a maintainer has to do, I want everybody to have bandwidth for, like, their passion part of the project, and right now we are far away from that, right? Right now, every hour, every minute I can spend on that is like trying to play a catch-up game. Yeah.
And that's this thing I really hope for, that at some point we can get to a point where we say, like, hey, we can… I mean, the other 6, they're also overworked and everything is complicated for them and whatever, but, like.
I have the feeling there's a lot of friction that does not have to be here, but we have to solve it, which is a lot of work, right? And that's, like, our… state right now, so understanding how others are addressing that is really, really helpful.
**Jack Baldry** 15:46 Yeah, and if you… you know, I know we've got a little bit of time now, obviously, to talk it through synchronously, but if you… I don't know how you tend to make these kind of bigger platform-level decisions, but if you've got, like, a design doc or something that might be the first step.
I'm very happy to get, like, more of my team to actually sort of get involved and see if that brings up things in there.
Like, from their experience.
**Severin Neumann (Bronto)** 16:11 which is…
**Jack Baldry** 16:12 You know, just a different lens to… Into the environment that we all share at Grafana. I think… If… and I can probably contribute some of… the things that I would personally prioritize if I was given a chance to greenfield stuff at Grafana. I think it… I'd love to be able to say that we did it.
In a good way, and didn't just build on top of, like.
**Severin Neumann (Bronto)** 16:37 Yeah, I mean…
**Jack Baldry** 16:38 an unstable base, and then we've got a lovely project that you could just adopt, and… or even, like, some core values, but I think… Yours… your situation is a lot more.
I do think you could eliminate a lot of the friction.
without taking on some of the frictions that we've got through, because you don't have private repos and stuff. Anything where you can… openly build the entire workspace, and then just work on optimizing how hard it is to build an entire workspace, I think makes the problem space a lot.
A lot simpler.
**Severin Neumann (Bronto)** 17:12 Yeah.
Yeah, no, I'm with you on that. Yeah, yeah.
There's, like, there's some advantages of not being in a corporate environment, for sure.
Umm.
**Jack Baldry** 17:21 Yep.
I'm sure there's a lot of disadvantages, too.
**Severin Neumann (Bronto)** 17:26 Yeah.
Yeah, I mean the biggest disadvantage is that like right now I mean the core maintainers of the SIG like we if we combine all our working hours that we put into that thing right now we maybe come up to a full-time person. I'm not even sure about that anymore.
And then we just lost two two long-time maintainers. So so so the the our biggest constraint has always been and and is is right now even more than ever is time.
So, even like thinking about re-architecturing is taking away time from just doing the things.
That everybody asks us to do every day, so… yeah.
**Jack Baldry** 18:09 Yeah, I think that is something to consider as well.
One of the… Affordances we have as a team in a corporate environment is that we.
can be on call for this, and so when problems arise, we can react in a… in a timely manner. If you're in a position where You know, things need to… Well, yeah, maybe it's worth designing around the fact that the time is limited, so it's more about, like.
Things happen when they can be managed, or… Or there's non-critical reliance on resources that… that aren't available, you know, 9 to 5 every day, like I get to have with my team, plus.
Plus, with NASA, we've got, like, basically full… full-time coverage.
**Severin Neumann (Bronto)** 19:02 Yeah.
**Jack Baldry** 19:05 I'm not sure what that means on a practical level, but it might be an aspect in the design of any systems you end up building.
**Severin Neumann (Bronto)** 19:13 No, I, again, I think one, one, one big, big design criteria for us is, I think, really like to reduce friction and also reduce overhead for us. I mean, that's my perspective, but… we… we had a very, very high bar for a lot of quality in our documentation. That's, of course, something that's really hard to sustain.
For all these things.
that you cannot test for, right? We have our, like, we have some tests, of course, for spell checking and And like then style checking and whatever, et cetera, et cetera.
But we all know that, like, actually what you really need, even if you have AI, is someone That reads through a document, end to end.
who is A not the author of it, and B also not like, a person at the same technical level, right? I mean, the moment we have had real technical writer like Tiffany in our SIG, like, the quality of, like, just… The technical writing just went up dramatically, because people are not, like.
engineers writing for engineers is always… people love saying that, but, like, there's a big risk to it, right? Oh, yeah. But at the same time, I said, we cannot sustain that for the whole documentation for the whole project forever, right? I mean, we just don't have… Enough people for that.
And again, I'd rather see people focusing on the key pieces, and everything else is just, like.
I don't know, in my perfect world, I would not even look at them. Like, they open up their PR, all the checks run, get green, a second person of that SIG looks at it and says, like, okay, to me at least, it looks good, and they merge it in, and we just take it, right?
And then we…
**Jack Baldry** 21:08 Yeah.
**Severin Neumann (Bronto)** 21:08 We can do better for the important.
important as always.
But you know what I mean, like, the pieces that more people are reading, or that are more… Core to, to everybody.
**Jack Baldry** 21:22 Yeah, and I do think it's really worth, exposing… the kind of data that lets people make that decision. I think trying to impose the decision-making of, like, what is important.
Could be quite challenging, and could be a really tempting sort of place to abuse numbers.
**Severin Neumann (Bronto)** 21:41 the.
**Jack Baldry** 21:42 Yeah.
**Severin Neumann (Bronto)** 21:43 Yeah, yeah.
**Jack Baldry** 21:45 And ensuring quality.
And I don't know if this is really… the kind of meeting you want to have where I'm sort of saying, oh, it turns out when we do it, it was always quite hard and painful, but… I'm not sure… so one of the things we do is, like, run Vail to try and enforce certain style, things across All of the repositories.
And… The… It's certainly, for a subset of The kind of style things you might want to enforce, it… is very good. But for anything semi-complicated, I think the maintenance overhead is really quite high.
**Severin Neumann (Bronto)** 22:25 Yeah, yeah, yeah.
**Jack Baldry** 22:26 providing.
**Severin Neumann (Bronto)** 22:27 We experimented with it a few times, we experiment… I think we're not using it still, I think we're still on text lint.
And really, really trying to… But because, as you said, like, there's a few rules in it that I really like, but I know exactly, like, the moment you flag that to people and say, like, hey, you should not say certain words, or you should not abbreviate it this and that way, and you don't give them, like, a one-click solution to fix it, then they're just, like.
tagging you and saying, like, hey, what should I do about that? And then, like, we're back to square one, so… Yeah.
**Jack Baldry** 23:01 Yeah, if you're not able to give them, like, super actionable advice in whatever CI you're building. It's… it will come back to you.
So often, especially if it's blocking. If it's blocking, you're going to cause yourself a lot of pain. Yeah, that's true.
**Severin Neumann (Bronto)** 23:15 It's our biggest pain with the link checker that we have, right? Like it's right now, Patrice is really doing his best to fix that. But it's right now. So we recently changed over to, how is it pronounced in English? Lucci. Lucci. Yeah.
**Jack Baldry** 23:31 Nucci?
**Severin Neumann (Bronto)** 23:32 But the thing is, like, it's really brittle, because sometimes it's like, oh, this check was happening at 3am, and the other one is now trying to put one at 3am, one minute, and then suddenly you have a merge conflict.
Which is just, yeah, not really, like, this thing we want to see.
**Jack Baldry** 23:54 Yeah, we've also had, like, link checking across all of our repos was one of the biggest challenges. Link checking For us, had to become a case of… Checking a subset of links.
Because of some… some things being private at certain times, it made the… Certainly, the feedback that we give at the pull request level Had to be a subset, and it could only be, like, a separate process.
**Severin Neumann (Bronto)** 24:25 Yeah.
**Jack Baldry** 24:25 That runs internally for us to be able to do, like, whole site checking.
And we ended up building… Another Go tool.
That's maybe a little hyper-specific to our environment, but it gave us the testing framework so that when we came up with a lot of the link checking edge cases, we could have the tests there that represented those specific edge cases. And all of the, sort of, like, off-the-shelf Link checkers.
Although they are very configurable, didn't, sort of allow us to properly capture the complicated… Contributing factors in our environment that, justified why this link could be checked and, why this link couldn't.
And why it was okay if it… if it broke.
So, unfortunately, I can't offer you anything particularly helpful there, either.
**Severin Neumann (Bronto)** 25:24 No, no, I mean, I mean, sometimes it's good to hear that people say, like, yeah, we have the same problems as you have, so…
**Jack Baldry** 25:31 you.
**Severin Neumann (Bronto)** 25:31 That just means, like, we're not doing something wrong here. If you now would have said, like, oh, link checking is a solved problem, do X, Y, and Z, and then I would be, of course, happy, but if you… if you also tell us, like, yeah, it's complicated, and it means, like, okay, we're not just… Going the wrong direction, so that's always helpful.
**Jack Baldry** 25:50 No, and if there is any, again, if there's any sort of… further, like, design document that may be focused specifically on link checking, I'm happy to get our teams to think on that with you.
**Severin Neumann (Bronto)** 26:03 And… Yeah.
**Jack Baldry** 26:04 In the, sort of, like, constrained space that you'll be working, because some of the.
**Severin Neumann (Bronto)** 26:08 Yeah.
**Jack Baldry** 26:08 You just won't be solving some of the things that we.
**Severin Neumann (Bronto)** 26:11 Yeah.
**Jack Baldry** 26:11 To… to work around.
**Severin Neumann (Bronto)** 26:13 Yeah, so in my mind, like, the one-minute rundown, like, how we should go about what we're doing right now. So Patricia said it's like looking into the link checking, trying to… To make something better here.
The next step that I think that we urgently need to do is, like, fix our… so I'm not sure how much you work with things like code owners on GitHub.
**Jack Baldry** 26:39 Quite a lot, yeah.
**Severin Neumann (Bronto)** 26:41 I hate them because, like, they require to give everybody right permissions, and if you don't give people right permissions, you cannot… So, so some point back, we switched into a different solution.
that's called component owners, which is, like, working with triage permissions, but then their PR reviews are not counted as, like, mandatory PR reviews, and so we are, like, back to square one.
So right now, my point of view is that, like, we get rid of any custom solution and just live with the fact that GitHub is screwing us over, and we have to give 150 to 200 people write permissions on our repository.
That's, that's just…
**Jack Baldry** 27:24 Yeah.
**Severin Neumann (Bronto)** 27:25 That's just the thing I think we start… we have to accept, so we have to clean that part up.
And then the next thing is, like.
We need to… we have a kind of bot, because another thing that GitHub is really bad at is, like, giving people limited merging permissions.
So we cannot say, like, oh, this person can only merge into this folder in this branch. No, you can merge or not merge. So there we are about to… or we started to test out some… Some auto-merge bot.
That's helping us with that. And when we have reached that point.
then I'm more confident to get back to the different special interest groups and say, like, hey.
You can now build your own workflows around that and like push code and like whatever do the things that you think are.
But that's right now my line of thinking. I might be too optimistic on that, but yeah.
**Jack Baldry** 28:30 Yeah, no, I think that's the.
because Codona's a ship, and so the merge part is so fundamental, it… it blows my mind that there isn't better provision in GitHub. They, proposed We got into a… I think it was still private preview of some feature that would allow you to Provide, sort of, more Control over who could review, like, who could count as an approval.
for certain subdirectories, but they limited it to something silly, like, I don't know, less than 20 rules.
**Severin Neumann (Bronto)** 29:02 Yeah, yeah, yeah, that feature now exists, and it also requires that person to have write permissions.
**Jack Baldry** 29:08 Yeah, still requires some time, right?
**Severin Neumann (Bronto)** 29:10 So it's not, like, really making any difference for me, right? So it's like… and there's, like, a bunch of outstanding issues for, like.
3 and 5 and 7 years, where people say, like, hey, can we not fix that?
So yeah.
**Jack Baldry** 29:24 Yeah.
Yeah, and some of those complicated, sort of, defining… specific rules. We've used PolicyBot internally, I think it might not have the right optics, to be honest, to be… for some repos, because it is a Palantir project.
**Severin Neumann (Bronto)** 29:43 Yeah, I saw that, and I was like, yeah, I'm not going to use that.
**Jack Baldry** 29:47 Yeah, I wouldn't use it in my own, personal projects. It… it… I mean, I like what it's proposing, which is, like, let's have the policy as a version-controlled object in the repositories, but… I don't see much movement on this either, and it has a bunch of limitations of its own when you're like…
**Severin Neumann (Bronto)** 30:11 Talking about…
**Jack Baldry** 30:12 Velocity, like, you can't have a maintainer update a branch without invalidating themselves from… Being able to review it, you know, by having a merge commit on the branch, now they are… A contributor, and therefore cannot be Like, if you need to have, like, a required one other person reviewer. You end up having to write some specific code to work around the case that a maintainer might want to just… move things along. So, if I were to do that myself, I'd end up building something. I haven't explored the space, though, to see if there's better Cooling. I do, actually, one thing that comes to mind is… We briefly explored, defining some policies.
that… we ended up with, like, a fairly simple Go wrapper around, but it was just evaluating, OPA.
And… We never got to… tidying up the repo. I think there was some references to some internal stuff that we needed to clear up.
But I think in theory that could be open sourced and sort of might serve as an example. I… go to lunch on a Tuesday with one of the engineers that works on OPA, and so he quite regularly gives me a Like, an elbow in the gut, and says, hey.
We'd love to see you open source this, because, you know, any example of OPA being used for anything is good for their project, so… Yep.
**Severin Neumann (Bronto)** 31:40 Yeah, that could be, that could be interesting as well. Yeah, yeah.
**Jack Baldry** 31:42 Yeah.
**Severin Neumann (Bronto)** 31:44 Interesting, yeah.
**Jack Baldry** 31:47 Yeah, and I think that I'd prefer to go that way if I had, Some time instead of Policy Bot, or…
**Severin Neumann (Bronto)** 31:54 Yeah, yeah.
But what I hear is, like, more or less, like… you're having… different but similar problems as we and have addressed a few of them.
But it looks like we're moving in a, in a good direction and whatever we are building, I, I, I'm, I'm going forward to, to share with this with you so we can, we can get some of your feedback on that.
**Jack Baldry** 32:20 Yeah, absolutely. I think you've got the priorities in the right order, and you've already identified, like, all of the I'm trying to… as you… as we were sort of going through, I was trying to think if we've encountered any sort of additional, specific Issues and I do think you've broadly caught all of them, it's, you know, the challenges of.
Things like link checking across all the repo, the challenge of maintaining velocity.
Yeah. While decentralizing things.
And ownership is, of course, a challenge, yeah.
**Severin Neumann (Bronto)** 32:50 Yeah.
**Jack Baldry** 32:52 it turns out that really, like, the… Putting all the website together for the build purposes is kind of the easy part, and then it's a lot of social challenges on top.
**Severin Neumann (Bronto)** 33:03 Yeah.
Yeah.
Yeah, yeah, no, okay, okay.
Good for like the future.
**Jack Baldry** 33:11 Sorry, yeah, I know you gotta run.
**Severin Neumann (Bronto)** 33:13 Dom.
I don't know if you, Tiffany, Jack, I mean you you can work into chat internally. So so so but but if you if you want to keep the conversation going, I I would appreciate that.
Yeah. But I would say, like, this was, like, super, super helpful. So, Jack, and especially, like, now knowing you, I know who to reach out to, so I highly appreciate that.
**Jack Baldry** 33:38 Brilliant. No, happy to be here. I'll work with Tiffany to see how I can be more available to you, like, so that you don't have to… yeah.
And I'll see how I can get my team to provide any guidance that they can.
**Severin Neumann (Bronto)** 33:51 Okay.
Okay.
**Jack Baldry** 33:54 Sweet.
**Severin Neumann (Bronto)** 33:55 Okay.
**Jack Baldry** 33:55 Well, thank you for having me.
**Tiffany Hrabusa** 33:57 Yeah.
Thanks for joining, Jack, we appreciate it.
**Jack Baldry** 34:01 Pleasure. Should I get out of here? I know you're also on your way at Severin, but to let you get to.
**Tiffany Hrabusa** 34:07 business.
**Jack Baldry** 34:08 or…
**Tiffany Hrabusa** 34:10 Yeah, I don't think the other topics will be of much interest, and I'm not sure how much we'll be able to cover.
**Severin Neumann (Bronto)** 34:14 No, most of them were from my agenda, so… but I wanted to focus on that, so I appreciate that.
Once again. Yeah. Yeah.
Awesome.
**Tiffany Hrabusa** 34:24 Vivek, did you have anything that you needed to discuss today?
**Severin Neumann (Bronto)** 34:28 I'm dropping now. Thank you.
**Tiffany Hrabusa** 34:30 Severin.
**Vivek Anandaraman** 34:31 No, no.
**Tiffany Hrabusa** 34:33 Okay, then I think we can call it a day.
**Vivek Anandaraman** 34:37 Sweet.
Cool.
**Jack Baldry** 34:39 Let's catch up some more Tiffany. Yep.
**Tiffany Hrabusa** 34:41 Absolutely. Have a good night.
**Jack Baldry** 34:43 Nice to meet you.
Bye! Bye!
**Tiffany Hrabusa** 34:45 Bye.
**Vivek Anandaraman** 34:46 Bye, guys.
