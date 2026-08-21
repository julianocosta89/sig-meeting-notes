SIG: Packaging SIG
Date: 2026-08-20
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado** 11:04 Aiden is.
How do you do?
Denise?
Do you know if this meeting is happening?
**Michele Mancioppi (Dash0 Inc.)** 11:24 I am.
**Diego Hurtado** 11:26 Whoa.
**Michele Mancioppi (Dash0 Inc.)** 11:29 Sorry for being late. I got stuck in a meeting.
**Diego Hurtado** 11:33 Can you hear me?
**Michele Mancioppi (Dash0 Inc.)** 11:37 Hi, Con.
Hi, Denise.
**Diego Hurtado** 11:44 Oh, boy.
Oh, by the way, Michele I am.
I should have the fix for… this issue with the minimum Python version today.
**Michele Mancioppi (Dash0 Inc.)** 12:04 I've seen your, your draft PR.
Yep. So, when you think it's ready, ping me.
**Diego Hurtado** 12:12 Sure. By the way, I… many times I… When I'm working on an issue, the first thing I do is open a draft VR.
So yeah, draft really means do not review it.
**Denys Sedchenko** 12:33 Do you hear me now?
**Michele Mancioppi (Dash0 Inc.)** 12:35 Yes.
**Denys Sedchenko** 12:37 I don't know why, but… Have problems with microphone on a laptop.
Just a quick disclaimer, the POC repo that I did based on the Cloudflare probably will be not available in a couple of days.
Because Cloudflare wants me to buy my Cloudflare Pro subscription, which I canceled, like, they're saying, like, no, like… If I'm not going to pay the bill, they will just clean up my bucket storage.
**Michele Mancioppi (Dash0 Inc.)** 13:24 Of course.
Because, like.
**Denys Sedchenko** 13:27 canceled my subscription right at the next day. They wanted to take money for annual subscriptions.
**Michele Mancioppi (Dash0 Inc.)** 13:35 Alright.
Well, we know it works, so… Good enough. And, there is the entire topic of, on which infrastructure we put that.
Which, Antoine, said he would, handle with Trask and the others.
So, my Nicholas there, might not be, who knows?
Did you have a chance to look at Launchpad?
**Denys Sedchenko** 14:03 Not yet, but I'll take a look.
Had a pretty stressful, busy week, I apologize.
**Michele Mancioppi (Dash0 Inc.)** 14:14 No, it's… look, I'm having the same problem, right? I'm, I'm underwater since a few weeks.
And I'm not managing to support you in this stuff at all, despite my best wishes. I'm sorry about it.
Today, ideally, the, Diego gets, the documentation, on Openterantry.io.
Which is cool.
there was a whole bunch of other PRs that I had to open in the background.
To set up all the permissions for that stuff, it is, it was not an easy… an easy thing. It was, like, twice, it was like, oh yeah, yeah, we need also to do something more with terraforms. Cool.
But that is sorted out, so now we are in a position where, we can just… Publish our docs should be relatively uncontroversial and unconscious.
**Denys Sedchenko** 15:22 The docs will be, like, in a separate repo for the docs repo, correct?
**Michele Mancioppi (Dash0 Inc.)** 15:26 It's on OpenTentry.io, so we're going to get a page, under, platform slash Linux.
Where we're going to put the system packages.
**Denys Sedchenko** 15:37 No, I mean, like, the source for the documentation, the markdown files.
**Michele Mancioppi (Dash0 Inc.)** 15:41 Yeah, they are in the OpenTyramids.io thing.
However, something that we could do, and it's something that in that Zero we do very successfully.
we could set up a small GitHub action that whenever we update the documentation from our repository, it creates a PR upstream.
the, it's not… it's never as simple as copying the README over, because there are different audiences.
But I would, myself, as well, prefer to have the source of truth for that in our repo.
**Denys Sedchenko** 16:26 Makes sense. Do we need to have, some kind of, like, a bot service account, so, like, that PR can be created on behalf of that bot?
Ideally, we need to… we need a GitHub app.
That will have, a permission to create PRs into that repo.
Last, probably… I assume the docs repo has some kind of CLA requirement, like, solution, like, sign contributor… Agreement license, and that bot needs to be excluded from it.
**Michele Mancioppi (Dash0 Inc.)** 17:03 Emigration.
**Denys Sedchenko** 17:03 No questions.
**Michele Mancioppi (Dash0 Inc.)** 17:05 I don't think it is super simple, because all the GitHub configurations, they are managed in the admin repo.
So it's not like I can go there and add my pat.
**Denys Sedchenko** 17:17 Yeah, I'm just giving the list of the problems, but, like, how are they solved is really… Depends on every organization, because everyone is doing it In a totally different way.
**Michele Mancioppi (Dash0 Inc.)** 17:30 Yeah, I don't know. That's a good question to ask Severin, if there is a plan to do that.
given the amount of manual things that I had to discover face first, I'm not sure that there is going to be a plan for that, but we'll see.
I mean, for now, given the fact that we're not updating very often.
So far, I mean, we haven't even published the first time.
I don't think it's a high priority, but eventually, especially when we go and document which versions contain which packages inside, then yeah, that is when it really needs to be automated.
realistically, the, the next two updates we would do is, one, when, Matt, manages to get, the, declarative configuration in Ruby merged, then we can make a Ruby package.
And the second update is going to be when we have a civilized place where we keep the packages. Until then, I don't expect much need of updates, to be honest.
**Denys Sedchenko** 18:30 Besides that, I was thinking about, like, decoupling my draft PR right now. You saw I have a draft PR, which basically bundles everything.
And I want to decouple… of the, like, I have some changes to the goal program that used to build package, I want to decouple the changes, so I can list for… I can list… get the first part merged, which just does the packaging without, like, specifying to what repo and, like, etc. So, like, the second PR can be, like, smaller.
**Michele Mancioppi (Dash0 Inc.)** 19:01 But my advice is, so these kind of things need to follow usually the rule of three.
So the logic starts making sense when you have 3 use cases for that.
now we know how it works in copper. I have not yet decoupled it until we know how it works in Launchpad.
I mean, we have Gita pages, check. Copper? Check.
The third is going to be Launchpad.
When we have a logic that can work on all three, it's gonna be fine.
**Denys Sedchenko** 19:31 For the launch pad… I remember there was a fork, Ubuntu fork, of the repo. I have to take a look at it.
**Michele Mancioppi (Dash0 Inc.)** 19:41 Exactly.
That is, when I say, hey, do you have a chance to look at launch, but I meant.pr?
**Denys Sedchenko** 19:50 Do you know if Sina is still with us?
**Michele Mancioppi (Dash0 Inc.)** 19:54 I don't know, it went AWOL. I actually had a chat with, With, the, VP of Engineering of Ubuntu over Signal a little while ago.
Actually, let me ask John right away.
Let's see what he says.
I also… some of the things that, that I heard is that, that Canonic was also thinking of, of making… putting our packages in, in a more official repo, so something like Universe or main.
That comes from an oblique reference where John told me, yeah, we think the injector is going to be very easy to package.
But the rest, not so much.
So, yeah, I think we need to… we need more representation from Canonical.
**Denys Sedchenko** 21:07 Also, considering that we're planning to add more packages for Ruby, for example.
I assume there will be, like, quite a decent lag.
Between our changes in what canonical puts, plus, like.
**Michele Mancioppi (Dash0 Inc.)** 21:22 It's not…
**Denys Sedchenko** 21:22 Snap package, so, like, the packages are for Ubuntu version, Yeah. Like…
**Michele Mancioppi (Dash0 Inc.)** 21:28 I'm actually… honestly, I think that's canonical, putting our stuff in a series repository is premature.
We do not have a versioning, policy.
in OpenTelemetry that is refined, stable, and consistent enough.
To be successful to do… to be able to successfully do that.
**Denys Sedchenko** 21:53 LSAT can be quite misleading for customers.
like… there are two ways to install Docker on Ubuntu. You have the official Docker.io package, but you've ins… like, but that package behaves like So-so. Or it's, like, ancient, or it's missing something.
So, like, there is a second way of installing official PPA.
of Docker engine. Well, basically, they behave differently, and you go straight to official PPA only, like, if you dealt with this problem before. If you don't, you'll fall into the trap of, like, how do you install Docker? What should I use?
**Michele Mancioppi (Dash0 Inc.)** 22:31 I don't know… yeah, I mean, the… We need to hear from them what they want to do.
I'm not, I don't know.
plus…
**Denys Sedchenko** 22:44 So basically, it will be tedious for support if we have two versions of packages, like in Ubuntu Universe and our own. And even in that case, probably our own will be, like, the primary version. We'll start saying to people, hey, just, like, install our official one.
**Michele Mancioppi (Dash0 Inc.)** 23:00 Yeah, that, that is the risk, right?
although the, the reach that, Ubuntu would give us, Is, is unmatched.
It's, I mean, that food to actually bring users. It's going to be painful as hell.
But it's also going to supercharge the visibility and also put pressure in the rest of OpenTelemetry to, you know.
Sort our shit out.
In terms of how something is injectable, the stability and quality of instrumentations, the versioning, thing.
That comes only from adoption.
So, are we going to crash into the… into a wall?
Yes.
Is it gonna teach us a few things that we need to learn probably the hard way?
I also think so.
In Italian, we have a saying that not all the bad things come to hurt you.
And this is probably… this would be one of them, I think.
**Denys Sedchenko** 24:07 Agree. If we'll have this problem, it means we succeed. It's, like, one of the problems you want… you want to have.
**Michele Mancioppi (Dash0 Inc.)** 24:15 It's a good problem to have.
It's a very… it would be a very good problem to have.
A massive problem, but a good one.
**Diego Hurtado** 24:23 Shouldn't the saying be… Not all the things that hurt you are bad.
**Michele Mancioppi (Dash0 Inc.)** 24:30 Are you talking about chocolate?
**Diego Hurtado** 24:37 No, I was, I was thinking about this Italian saying you just mentioned.
**Michele Mancioppi (Dash0 Inc.)** 24:42 Yeah.
Not only come to, to, to render, to render bad on you.
**Diego Hurtado** 24:51 Yes.
I think it would be the other way around, like, not all the things that hurt you are bad.
Which is true.
**Denys Sedchenko** 25:00 How that doesn't kill you makes you stronger, Zenichi said.
**Michele Mancioppi (Dash0 Inc.)** 25:05 Yeah, that makes you stranger.
That's the correct way to put it, since Batman.
All right. Do we have any other, other things going on?
**Denys Sedchenko** 25:17 Do you know, like, I saw that, like, there was a ticket actually give us permissions and, like, orgs made by Antoine.
Do you know, like.
**Michele Mancioppi (Dash0 Inc.)** 25:33 I mean… Let me check. We should actually start, we should get into the habit of starting these calls with Riage.
Looking at the issues that we have, because we… we tend not to.
So let me put it on screen.
Let's go.
Who requests?
This is what Diego's working on. This… the verified Java agent GPT. This one, this guy, whom unfortunately I don't know the name of, your name is Matthew. So, he already did it for .NET, but for Java, I asked him to go and open upstream, an issue for the Java agent to actually publish the checksum?
As a release artifact, because… This PR is doing some… Strange things.
To… to cover the issue.
**Denys Sedchenko** 26:40 Yeah, like, with… you mean, like, the shotsums.txt file?
Yeah, with Shastaunch.txt, you don't need GitHub API to actually, like, fetch the artifacts for a convenient thing.
**Michele Mancioppi (Dash0 Inc.)** 26:53 Yeah, no, I mean, this is overly complicated. I would prefer the, the Java agent to publish a, a SASAM, and then just go with it.
This one, Antoine, I understand, is on vacations, so it's, it's going to… I already commented, made a bunch of comments, because I don't think it goes hard enough in giving a good experience.
This front one to make the next iteration.
This one, Diego.
it's failing the builds, but this is probably a transient failure. This is something we should look at it again, right?
Alright.
And maybe it's something you and I do offline?
**Diego Hurtado** 27:47 Yeah. I couldn't… I've still gotten to the point of my GitHub notifications, but I'll… I'll just jump straight to it.
**Michele Mancioppi (Dash0 Inc.)** 28:00 Then, let's see, issues, if there's something new.
Okay.
then I think we are done for today.
Right?
Good. Done, folks. next week, I'll be off.
So I'm going to skip two installments. I'm back on the week of, september the 7th.
**Denys Sedchenko** 28:33 The same.
**Michele Mancioppi (Dash0 Inc.)** 28:35 Good, done.
Probably will.
**Diego Hurtado** 28:38 I'm here.
**Michele Mancioppi (Dash0 Inc.)** 28:39 After the SIG Meetings.
Alright.
**Diego Hurtado** 28:42 Actually, the… the… If you will… if you decide that, it'll be great for me to know, so that… I couldn't name those.
**Michele Mancioppi (Dash0 Inc.)** 28:50 all of the SIG Meetings were posted in the channel, right?
**Diego Hurtado** 28:53 Okay, okay, alright.
**Michele Mancioppi (Dash0 Inc.)** 28:56 Actually, you know what? Let me, let me put it here.
I'll put it directly in the packaging.
I'm gonna dump it on Antoine, Antoine.
All right. Bye folks, see you in September.
**Diego Hurtado** 29:32 Baby.
