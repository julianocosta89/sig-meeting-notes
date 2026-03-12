SIG: Governance Committee
Date: 2025-08-13
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 01:10 Hey guys.
**Austin Parker** 01:12 Odie.
**Dan Gomez Blanco** 01:54 Good morning.
Afternoon, evening.
**Tigran Najaryan** 02:00 Hi, Don.
**Austin Parker** 02:01 It's… some time of day.
**Dan Gomez Blanco** 02:03 I'm of a day somewhere.
It's beer o'clock somewhere.
**Austin Parker** 02:09 God, I wish.
**Trask Stalnaker** 02:13 I would like to go there, wherever that is.
**Pablo Baeyens** 02:29 Third, do we want to switch to a private session, then?
**Josh Suereth** 02:37 If we have public topics, we can do those first.
**Tigran Najaryan** 02:40 Yeah, I think Dan has something, right?
**Dan Gomez Blanco** 02:43 … yep.
**Tigran Najaryan** 02:46 Yeah, we're kind of stuck with that.
**Dan Gomez Blanco** 02:48 2… Actually, I will link the PR there. One second.
Right, so, yeah, I just wanted to discuss the, there was an issue opened, I guess this is part of the… Part of the graduation process, … by Emily, basically… To document the roadmap management, … or the process, the roadmap, management process. So I open up PR, and then basically building on what, building up on what Austin did, and short, like, I think a couple of weeks ago.
… that basically, yeah, I'm syncing… different aspects of, like, projects to, to, like, basically rolling that up to a project view, so it's easy to see, you know, what OTEL is working on.
I open up PR there to… Mmm… change, or basically reword a little bit the project management, but also add a document for roadmap management, and including the stuff that we, you know, basically, how do we… how do we manage those items? I guess the major change that I wanted to discuss, and this is why I only put 10 minutes for this topic, which… we could talk about for longer, is that that relies on everything, every roadmap item being backed by a GitHub project.
So, that could be an OpenTelemetry-wide project that we, you know, we always have, like, project boards for those, or it could be a SIG that decides to work on a particular, like, high importance item, and I have a GitHub project. But as long as, basically, that introduces a change to the sex.yaml, like, the file that we've got in the community repo.
And that would, basically list these project boards, right? So, if a SIG takes on something that they want to advertise more widely as hey, we're working on this, this is our focus, they can add it to the 6.yaml, and that will get rolled up into a view.
That we can report on with some start… tentative start and target dates.
Mmm… So, if I… I can probably share my screen.
A second and show you what that looked like.
So I'm… I've done that with… yeah, so this one, for example, this is only taking the… the project… it doesn't take anything that a specific SIG may be working on. This is only taking the projects that, … that are currently… In the project's folder, as in, like, in the community repo.
And so, for example, if I take the case of M… Yeah, Arrow, for example.
M… That syncs the… The short description of a project here, the readme of a project, and as well, the start If I can click on that, well, that'll go into the Autel Arrow repo, but … That will sync the… the, start and end dates. So basically, see how here this has got a status?
So that would be like… M… the start date was March 31st, 2025, and the target date is September 29th.
So that sinks.
This issue, or this, basically this thing from the, from the project itself.
And then people could go in… into this and find more things about the project, right?
Mmm… So yeah, … That is, if you go through that PR, basically the PR that's opened, And….
**Ted Young** 07:06 Where does it scrape the start and end date from?
**Dan Gomez Blanco** 07:10 … from the….
**Austin Parker** 07:12 Start date was from… Or is this my thing?
**Dan Gomez Blanco** 07:16 No, this is the one that I built that is inspired by that.
**Austin Parker** 07:19 Oh, okay.
**Dan Gomez Blanco** 07:21 But it's more like, for example, this one, so it scrapes it from the projects.
Status. So, if you.
**Austin Parker** 07:30 Oh, yeah, yeah.
**Dan Gomez Blanco** 07:32 So let's say this is the CICD CENCOM seg board, and then you can… Add an update and say, okay, well, this is now… At risk, but in the end.
**Austin Parker** 07:43 Someone has to add that.
Yeah. Or someone has to put that status update in.
**Dan Gomez Blanco** 07:47 Yeah.
**Austin Parker** 07:47 Yeah.
**Dan Gomez Blanco** 07:48 And I think this could be… this could be good for… because that basically means that… project leads can keep, you know, that more up-to-date without having to open a PR to update the expected timelines.
**Austin Parker** 08:00 Yeah.
**Ted Young** 08:03 So, so I've been circulating this, and… I think people… Are generally like the idea about getting more organized.
And I've heard back from SIGs that they're… they're often reluctant to create, like, a project or project board or whatever, because it's just kind of, like, a lot of work.
Essentially. But if there was… You know, something they got out of doing that work, that's some motivation.
But Sorry, go ahead.
**Dan Gomez Blanco** 08:36 Yeah, I'm not proposing that they, you know, for anything that a SIG wants to work on, I'm not proposing that they create a full, like, you know.
and this is probably something that I wanted to talk about, is that, let's say that a SIG wants to focus on one thing that's scoped to that SEG alone.
I don't think they need to create a project proposal, get the approval from the TC and GC and all that.
They should be able to just create a project board.
set the start date and end date, and then just work towards those deliverables themselves? As in, like, fairly low process there?
**Ted Young** 09:08 Right.
Exactly.
… So, but, the other thing… I was running into a bit was just some confusion, possibly stemming from the fact that we're using the word project now to describe, like, 5 different things.
**Dan Gomez Blanco** 09:27 Yes.
**Ted Young** 09:28 the OpenTelemetry project, you have GitHub projects, you have projects that we're making within OpenTelemetry.
They create the project boards, and now we have two tiers of… those kinds of projects, right? We have, like, TC projects, right, projects that… You know, basically require us to get involved in the organizing, because there's some kind of new effort.
And then there's, like… projects from, like, ongoing SIGs, where, like, as long as the… TC, GC, everyone involved in that SIG is fine with it.
they can keep moving. So I just… I wonder if we need to come up with some words other than project to describe these things.
**Dan Gomez Blanco** 10:14 I… when I was… yeah, I was working through this, and I think I… this is the roadmap management… the project management… sorry, the project management, guidance, and I added something here to clarify some of those things.
But as I was writing this, I think there are, like, in this document alone, there are, like.
250 mentions of the word projects. Yeah. Meaning different things, so maybe, I don't know, like, the thing that….
**Austin Parker** 10:44 Yeah, I don't wanna, like… cut off discussion on this, but what I would… I would like to do is just emphasize that we need to, like.
It's okay if we are not completely right, or that this is maybe that we need to change this later.
Great. If we need to change it, we can change it, it's just the repo. We need to, like, act.
**Dan Gomez Blanco** 11:07 Yeah, so I think….
**Austin Parker** 11:08 Yeah. Like, we need to just take this and run with it.
**Dan Gomez Blanco** 11:11 Yeah, I think the, as long as we can create I mean, even the projects themselves, as in, like, if you, you know… but I mean by that, I mean, like, project boards, and, like, GitHub projects.
Even if we can just create them now for the roadmap items we've got, and have some target and end dates, that, you know, that we can sync to that overall view.
then, you know, that can get us somewhat, right? I mean, that's… that's the bit that… Then we can fill in the details later, right?
**Austin Parker** 11:40 Yeah, yeah, just… the important thing right now is that we have this… that we have the process document, and that we can point to the process document and say, hey, this is the doc… this is the process, and the process can involve, but, like… We are… trying to make a deadline. We are trying to meet a deadline, and the deadline is getting closer, because they… if we would like to graduate by KubeCon, then we need to get this shit done. Right. So….
**Ted Young** 12:08 I think it's totally fine to kind of, like.
race this through, but then have, like, a follow-up issue or PR to discuss some of these things.
**Austin Parker** 12:18 Please buy us to action, thank you.
**Ted Young** 12:21 Yeah, 100%.
**Dan Gomez Blanco** 12:23 If we… if we can… review that, I can move that roadmap project into, like, the one that I created into Hotel.
Because it's not in my personal org. And then, you know, we can start syncing that, and then, yeah.
**Ted Young** 12:39 Yeah, this is just my feedback, and we can move this discussion to GitHub, but the things I've noticed, and we could do this as a follow-up, I'm totally not blocking things, is one, people are, like.
confused about the wording, right? And what they're specifically confused about is, like, when do they or do they not When does a project need to… go through TC sponsorship and all of this, and when does it not? I think we should use a different word to describe these things.
**Dan Gomez Blanco** 13:11 I think so, too, but ….
**Ted Young** 13:12 And the other thing was, like, having to go to the community repo and make a PR and mess with something, versus being able to, like, keep this stuff maybe within your own repo.
is another thing that maintainers, I think, will have some opinions about.
Or at least as a barrier to, like, getting them to, like, use it.
**Dan Gomez Blanco** 13:33 Yeah, hopefully this… this, approach that I'm putting out there is… should be fairly… Low friction for maintainers already, so… Totally. And then I'll… I reached out to some of the SIGs, some of the ones that we have projects for already. They don't have start or end dates, so they are, like, … they need reviewing, basically.
I know that, Josh, reached out about the… I think you're… you were… Looking at the entities one.
Yep.
But yeah, so, I'll keep reaching out to the rest, I'm happy to follow up on that as well.
**Josh Suereth** 14:10 Yeah.
For context, I just want to say I love what you're doing, and I echo Ted's concerns of, we found a lot of value in driving, like, entities, directly in the project, and focusing people in there.
**Dan Gomez Blanco** 14:24 So, by having the SIG mean almost revolve around it.
**Josh Suereth** 14:28 we get people to pay attention to what's in there, and actually make progress on tasks. So, if we can tie that into how we do Roadmap, I think that'd be awesome.
**Dan Gomez Blanco** 14:38 Yep. Cool.
Are there any other….
**Austin Parker** 14:44 Graduation things that we do, yeah.
So… Hi, Riley. Hi, Trask. Remember when we were under the impression from SecuritySig that Scorecard was enough?
Well, that's not actually true. I have been informed that no, scorecard and CLO Monitor are not what they want to see, they want to see passing OpenSSF best practices badges for all of our core repos. This is a hard requirement.
….
**Trask Stalnaker** 15:17 All… all repos?
**Austin Parker** 15:18 All core repos.
**Trask Stalnaker** 15:20 Core repos, okay.
**Austin Parker** 15:21 And the core repos are where we get to define those, so all we need is spec and proto.
**Trask Stalnaker** 15:28 And Python?
**Austin Parker** 15:29 And Python.
We could always kick Python out of core if we had to. But we need, like, that's a, like… please, if we people could rearrange their priority list for this, and I understand that I am making an ask that I am not willing, that I am not able to do, but I am… Unfortunately, until… early to mid-September, oversubscribed about 20 different ways, so I am going to have to beg of other people to do this work for me.
**Reiley Yang** 16:06 Can you link to the source of truth? I want to understand.
**Austin Parker** 16:08 It is at bestpractices.dev site I linked.
**Ted Young** 16:12 Cool. Do you mind creating an issue or something on Community to track.
**Austin Parker** 16:16 I… yeah, I will….
**Ted Young** 16:17 It's not already there.
**Austin Parker** 16:18 I will create one. I don't know if there is one already, but I will create a new one.
**Reiley Yang** 16:24 I mean, if you look at the… If you look at the status, there's a passing, there's also silver and gold.
**Austin Parker** 16:31 Passing is what we….
**Reiley Yang** 16:32 clear.
**Austin Parker** 16:33 We just need… I think passing is the lowest one.
**Reiley Yang** 16:37 Okay.
**Austin Parker** 16:39 ….
**Reiley Yang** 16:40 And can we write it down?
**Austin Parker** 16:41 I will write down… I will write this down, and then, … Make sure that the… TOC is aligned with this, but I've been talking to them… I've been talking to them, to our TOC, the TOC members that are working on this, in a different channel, and… trying to organize it. They are also sorry that, … We were given that impression about what is… What? Bud?
They are sorry anyway, where they are going to go talk to them and be like, hey….
**Trask Stalnaker** 17:21 That's fine. I've… I've filled out, … Four or five of these.
**Austin Parker** 17:25 I, I know.
**Trask Stalnaker** 17:26 a repo.
**Austin Parker** 17:26 I know, they suck.
**Trask Stalnaker** 17:27 They're just… it's just a big questionnaire, like… It's a big questionnaire, yeah. You know, 150 questions, that are not super relevant to SDKs, so, anyway, yeah.
And even more so not relevant to the spec and proto repos. I could probably cover those, just.
**Austin Parker** 17:49 But that's been….
**Trask Stalnaker** 17:49 that questionnaire enough. The Python one, we would need an actual Python maintainer to fill out.
**Austin Parker** 17:55 I had a very similar conversation.
**Trask Stalnaker** 18:02 That's fine. I'll do the… I'll do the proto… I'll do the proto and spec ones, just because I… Read through those questions.
**Austin Parker** 18:10 Thank you.
**Trask Stalnaker** 18:10 Enough times already.
Probably take me the least amount of time.
**Austin Parker** 18:17 That's all. And I really appreciate all the work everyone is doing on this, and I am… Again, apostari for, being… Having less bandwidth for hotel stuff, but… It's a busy time at work, so….
**Trask Stalnaker** 18:32 Yeah, just send the community issue.
**Austin Parker** 18:35 That's all I had.
We're, we're so close, we're so close, I can taste it in the air.
**Pablo Baeyens** 18:41 Is there anything else that we can do? The adopters interviews? Is that…?
**Austin Parker** 18:46 Has everyone felt, if you had adopters, opt-opters… That you know were on that list, just run them down and see… make sure that they got contacted, or if they didn't.
Just tell them to be aware.
**Ted Young** 19:04 Where's the… where's the list?
**Austin Parker** 19:08 We don't have access to lists, I don't think. It's a list that they… we told people to… it was, like, Google Form, right?
**Dan Gomez Blanco** 19:16 Yeah.
**Austin Parker** 19:18 But I don't think it's a… it's not a Google form we created, it's a Google form the TOC did.
**Ted Young** 19:22 Ma.
**Pablo Baeyens** 19:23 There's so… thread in the GC channel with… The ones that we….
**Austin Parker** 19:29 Yeah, I know, and I believe they've reached out to contact some of them, I just… again, this is more of a, if you personally know any of those people, or whatever, and would like to… Like, run them down and say, like, hey, did you… Did you get… A thing, are you being responsive?
**Trask Stalnaker** 19:49 Riley, could you ping Kennedy? I pinged him a week or so ago, but didn't hear back.
**Reiley Yang** 19:57 On what?
**Trask Stalnaker** 19:59 on this… on if the CNCF reached out for the… didn't we submit Kennedy as a adopter?
**Reiley Yang** 20:07 I'm not sure.
**Trask Stalnaker** 20:09 For adopter interviews? Okay.
**Reiley Yang** 20:10 I can't check with him.
**Trask Stalnaker** 20:13 I'll start out… Chat.
**Reiley Yang** 20:17 Okay.
**Trask Stalnaker** 20:17 with us.
**Reiley Yang** 20:21 Yeah, I have a question for the… for the open SSF best practice, … like, currently, whoever created the initial project under that best practice will have access, and I wonder if there's a way that we can either group our folks.
Like, I… I… I added a couple of projects there, and… Let me share the link here.
**Austin Parker** 20:50 Did I transfer who… Yes.
**Reiley Yang** 20:54 So I….
**Austin Parker** 20:55 thing?
**Reiley Yang** 20:55 I shared a link in the chat. If you open that link, you can see each project listed there. They have an owner.
**Austin Parker** 21:02 Yeah.
**Reiley Yang** 21:03 The first one is, like, Carter for OpenTelemetry collector, so my question is, do you know if there's a way we can transfer the owner, and we can grant access to other folks? My worry is, what if people leave?
**Austin Parker** 21:14 … I'm sure there's a way, I just don't know how. We can probably… ….
**Reiley Yang** 21:28 I mean, CNCF, like, who's asking for that? They probably can't help, right? We can ask them, like, you asked for this, and we're trying to work on that, but we want to know how to change the owner. I searched the webpage, I couldn't find that.
**Austin Parker** 21:43 Yeah… I….
**Trask Stalnaker** 21:44 Riley, … the… anyone… I think anyone who has write permission to the repo, or maybe as a maintainer or higher, has permission to edit it.
Like, I can edit the collector one, I don't know if I can change who is listed as the owner.
**Austin Parker** 22:05 I will open an issue on their repo, on the best.
**Pablo Baeyens** 22:09 It's already an… an issue….
**Austin Parker** 22:12 Is there an issue about….
**Pablo Baeyens** 22:14 I sent it on the Zoom chat, and there's a response from last year saying, we can change the owner to someone else, we just need evidence that the new owner should be authorized. You can just email the guy here.
**Reiley Yang** 22:25 Okay.
**Austin Parker** 22:26 dwheeler at Lenoxfoundation.org. Yeah.
The owner at editor, then add more editors.
I think we should probably just… I need to use her, right?
**Trask Stalnaker** 22:42 But I don't think that should block us, because….
**Austin Parker** 22:45 No, I think we….
**Trask Stalnaker** 22:46 ….
**Austin Parker** 22:47 I just… create a… we should probably just have, like, a service account or something? I don't know if….
**Pablo Baeyens** 22:54 I also have permissions to edit the collector one, so….
**Trask Stalnaker** 22:57 Yeah, I don't think we need a service account, Austin, because anybody… it's based on your GitHub permissions.
**Austin Parker** 23:03 And you have.
**Trask Stalnaker** 23:04 It writes to it.
**Austin Parker** 23:05 Okay.
You notice?
**Trask Stalnaker** 23:09 It's just, there's just an owner listed, but I'm not sure that's really too relevant, who the owner is.
**Austin Parker** 23:15 Oh, I should probably get Carter off there.
**Reiley Yang** 23:17 So if there's an owner, and they don't have access to OpenTelemetry anymore, do they have the access to remove that entry or something? It's just unclear.
**Pablo Baeyens** 23:28 But not a blocker. David Wheeler.
Person.
**Austin Parker** 23:34 We would probably just need to contact someone at CNCF.
**Ted Young** 23:38 He's saying… Yeah, David Wheeler's saying, I need the user ID number of the new owner on the OpenSSF Best Practices Badge. Create an account on the best practices badge site login, see your profile, you'll see it. I also need evidence that this is an authorized transfer. So this is not something automated. Yeah, they….
**Austin Parker** 23:59 There's probably someone updating something in a database manually.
**Ted Young** 24:02 You have to poke this… this guy, and be like.
here's some social evidence that's hard to manufacture that proves I'm… You know.
Actually, the new owner of this thing.
**Trask Stalnaker** 24:25 I did question the Riley's question of if the prior owners, lose… access to edit it once they lose GitHub access.
Because if they lose access, then at least it's not a worry, but if they maintain access for some reason, then….
**Austin Parker** 24:45 Sounds like a good question to file an issue for.
**Ted Young** 24:50 Well, if it's dependent on their GitHub.
**Austin Parker** 24:54 I mean, yeah, but like….
**Ted Young** 24:55 Carter, I think, is….
**Austin Parker** 24:57 Not in the org anymore?
**Trask Stalnaker** 25:02 He's in the org, but he probably doesn't have right permission to collect her.
**Austin Parker** 25:06 Yeah, so, like….
**Ted Young** 25:10 You might want to double-check, he might still… Might still have it.
**Austin Parker** 25:22 Anyway, that's all I had on this, just… I created an issue, I put the link in the meeting notes, but… Really appreciate people's, … Continued dedication to this.
That's all I had.
**Ted Young** 25:43 … I had a short topic that's more just GC only, right? So, I would like to release this prospectus for OTEL Unplugged, so… TC might not have heard about this, but we're trying to get… because… a more of, like, an un… an unconference project planning meeting, hearing back from the community kind of thing. We used to have a lot more of this at KubeCon, but they kind of got squeezed out of the schedule. So we want to have some unconference events, where we can do this, and we're gonna try running them on our own. Grafana Labs is gonna host the first one.
But the deal we want to work out is that, like, a company hosts it, aka they deal with the venue and the ticketing and the catering and all of that, but the hotel GC is in charge of, like, actually running the event.
… and different… Organizations can host these things, and maybe we can use this first one as kind of a template.
To that end, the prospectus I'd like to send out for this, I'd like it to include a note from the GC.
You know, just being like.
how cool this event's gonna be, essentially, but also making it a little bit clearer, this is, like, a community meetup, not… not a Grafana Labs… going rogue and grabbing the OpenTelemetry brand, and… Being weirdos.
So I think having a little blurb in there, but… this is a GCTC meeting, so we don't have to… use this time for that, but I might just write a little version of this where someone else can splat something in there, and then I'll get the approval from the GC asynchronously.
And, Dan, I know you already were asking me, like, hey, people want to sign up to sponsor this thing, who they talk to, and I'll get you that info back, but it was just like, we technically have not actually, like, put the prospectus out yet.
**Dan Gomez Blanco** 27:56 I have.
**Ted Young** 27:57 But I'm stoked that there's enough interest that people are poking me and being like, take my money.
**Pablo Baeyens** 28:05 I'd be interested in that as well. So, yeah, you can share it with the GC Tunnel whenever you have it.
**Ted Young** 28:10 Yeah.
**Dan Gomez Blanco** 28:11 Awesome.
**Ted Young** 28:14 Cool, that's what I got.
**Dan Gomez Blanco** 28:16 Easter.
**Trask Stalnaker** 28:23 I think the next topic is mine. Just real quick, … TC, do you want, to assign a… I didn't want to merge it without, getting confirmation from you all if you want to assign a TC sponsor before we merge it, or, follow up after.
**Josh Suereth** 28:47 … I… I do want to talk about this, … a little bit more. I think we have a, … an issue where, I know that someone reached out to me very angry about this being blocked, about TC sponsorship. Made a lot of strong-worded comments.
And I dealt with that.
**Trask Stalnaker** 29:09 Sorry.
**Josh Suereth** 29:09 … I think, to answer your question initially, I think if something existed prior to the requirement sponsorship, feel free to push it through, and we'll address it later, just to keep things moving. But I do think we should have a sponsorship here, and I think we'll have to find a way to, explain this to the community of, like, what the goal of this is and all that kind of stuff. I did share, like, the original pull request and things, For feedback, but yeah, … There was a phrase that was sent to me that said, you are in my way.
And I think we need to address that.
**Dan Gomez Blanco** 29:49 Oh, yeah.
**Trask Stalnaker** 29:53 This particular project, I actually… I'm not really sure that it existed before. I mean, this… adding it right now… is sort of… we didn't have a GC liaison until this PR was created.
So that's… why I was… I was blocking it for, you know, asking, basically, for whether TC wanted to jump in.
**Josh Suereth** 30:21 we talked in the TC, and I tried to have this discussion, which… got a little sidetracked, but basically, the TC's opinion is, if this project is going to be impacting configuration in OpenTelemetry, we think it should probably have guiding sponsorship, or more significant sponsorship, because it needs to cross a lot of SIGs. If the initial deliverables don't involve that, which I've been told it doesn't.
We think it only needs an escalating sponsorship. And it probably should be someone, you know, related to the, … the operator. So, I think this only needs escalating sponsorship. I think it's fine to move forward as is, and we'll get a TC allocated to it. But I will say that this was another kind of communication breakdown that we should probably address.
**Dan Gomez Blanco** 31:05 Makes sense.
**Trask Stalnaker** 31:07 Okay, go ahead.
I was just gonna ask to follow up on that separate topic in the GCTC channel.
**Ted Young** 31:19 Okay.
**Dan Gomez Blanco** 31:20 just, … I know that we're… we've got the other topic to discuss. Just one last thing in the PR that I sent before, the one about the… the roadmap process, and… and all that, there is, like, a re… like, something basically that we're adding there to… To explain a little bit of the sponsorship for projects.
And I hope that aligns with the TC sponsorship as well. Now, there's one aspect that hopefully, you know, you can review, but it's related to what happens if an existing SIG.
opens up.
a new project, right? Is that, like, automatically get sponsorship, because a SIG is already sponsored? Like, a SIG that has a TC sponsor.
Opens out a new project proposal.
can we assume that the TC sponsor is the one that there's the, you know.
that's the sponsor for the SIG, or… yeah, so anyway, don't want to take more time on that, but, if you… if you have any comments, please add them to the PR.
**Ted Young** 32:16 Yeah.
Yeah, I'd like us to move to the private, topic, but, it would be great to maybe do, like, an offline or an async post-mortem on this, Josh, because, you know.
We don't want people upset about the process, we want to clarify it more. Also, if there's just big personalities in that group, it's almost like Exhibit A on, like, why we might want To be keeping track of them.
But I do think this gets back to, like, clarifying things, and maybe it's different words for these different levels of projects. But I actually see this as, like, a positive thing around being like, hey, if your SIG can restrict itself to this scope of work, then you only need an escalating sponsor, or you can just continue on with your existing stuff within your SIG.
But if you want to expand out to all this other shit.
well, that actually requires more attention, so I think it's, like, a great filtering function to keep people focused.
But we need more words to make it make sense to people.
**Josh Suereth** 33:21 I absolutely agree. That's what I wanted to say, was I think, … the message we need to send around this is making sure that we are… our attention is actually, I think, our most precious resource across all of the OpenTelemetry maintainers. And so, it's not just about the TC being able to pay attention, it's about the maintainers. And so, if you're going to propose a new project scope, to Dan's question, right?
if that project scope expands the number of maintainers that are involved in the SIG, or that the SIG is impacting, we have to evaluate the size of that at that point in time. So, I think we, like, we can't just greenlight them, necessarily. We need to make sure all the stakeholders are involved. That's the idea behind this. So.
It doesn't necessarily need to be the TC sponsorship that could change. We should care about the maintainer sponsorship. If, like, the operator SIG proposes something that has a lot of collector work.
We need the collector maintainers to sponsor it, right? So we should do a sponsorship evaluation on projects, and part of that will be TC, yeah.
**Ted Young** 34:21 But we also just need to make sure that this process doesn't start to look scary to maintainers, right? Because if it looks like, oh, you stick your head up, and then Management comes in and starts bossing you around, and like… being annoying, then it's, like, discouraging people for….
**Josh Suereth** 34:38 Agreeing, and I think that's the message that was sent and not intended, that we had to work through, yeah, so we should talk about that. Yep.
**Ted Young** 34:47 Okay.
Cool.
Private topic.
**Tigran Najaryan** 34:54 I think Riley has something there.
**Reiley Yang** 34:56 Yeah, very, very quick topic. Let me share my screen.
Can you sit?
**Armin (Dynatrace)** 35:05 Yep.
**Reiley Yang** 35:06 Yeah, so I have a PR, a small one, so please help to take a look. My goal here is, I noticed, like, most of the repo maintainers, they don't seem to have clarity regarding Like, how do they prioritize security problems? And currently, TC kind of have the rotation, so we have a monthly rotation.
we look at the security advisories. These are whoever using OpenTelemetry to create a security issue on GitHub, but there are many existing security vulnerabilities that nobody created an issue. It's just, like, discovered by dependent bot, or someone, like, in a certain repository is using library dependency that has never received any update in the past 10 years. So, I want to give a summary of the holistic view, like, what are the potential security vulnerabilities people as a maintainer, should care about, and also set some expectations. I put some, like, Uber timeline there, like, … Like, couple weeks, or for critical ones, and maybe a month for For medium and low.
severity ones. So, I want to get feedback from this group, and if we have a general consensus, or, like, we believe this is the right balance, then after I merge this PR, I want to talk in the SPAC and maintainers meeting.
And in addition, so we created this dashboard. Currently, it only has one column, which is the scorecard, but once we agreed, I want to create an additional column showing people these are the number of security issues you have.
And these are the things that you have to take action in two weeks. These are the things you have to take action in a month. So just have something more actionable for the maintainers, and have a place for us to track the action, so we can maybe do a weekly review, like, spend a couple minutes in the maintainers meeting.
So far, I got feedback from Army, so I appreciate that. I want to get more feedback from folks.
That's all.
**Trask Stalnaker** 37:24 Yeah, we can talk more in security, but my, … feedback in general is, I think it would be helpful to Roll this out, like, to a couple, like, pick two repos, one or two repos, to roll it out to first.
To test that before we make a big, like, … broad ask all… asking all repos to onboard to this. Yes.
**Reiley Yang** 37:54 So… so here's my thinking. I want to get the initial feedback from TC and GC to see if this is even the right direction we want to make investment. And if the answer is yes, I want to merge this PR, knowing that it's a draft thing. And then I'll… I'll… find a couple maintainers to give a try and collect feedback, and if we have some proven success, then I'll go to the broader meeting to share. Currently, I'm stuck. I have this PR, only got feedback from Army, it's been there for a while.
So, I want to get feedback, so I would know if you even agree with this direction, or you think this is not something we should spend time on.
Okay, thank you.
**Tigran Najaryan** 38:45 You guys have the link to the private Zoom?
**Austin Parker** 38:49 I'll start one, I'll put it in GCTC chat.
**Tigran Najaryan** 38:54 Thanks.
**Trask Stalnaker** 38:54 Okay.
**Reiley Yang** 38:55 See you there. Thank you.
