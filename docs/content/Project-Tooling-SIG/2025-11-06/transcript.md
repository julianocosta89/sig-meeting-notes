SIG: Project Tooling SIG
Date: 2025-11-06
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:03 Antoine!
**atoulme** 01:06 Ditto!
**Trask Stalnaker** 01:07 Howdy.
**atoulme** 01:09 I'm on mute? No. I'm not on mute. Okay, hey, Trask.
**Trask Stalnaker** 01:13 Hey.
**atoulme** 01:14 So, I'm playing go-between between mainframe and you at this point.
Okay.
not great, but this is what it is. I'm trying to make sure that Rudiger is doing the work of setting up the GitHub Action application for this.
So there seems to be a bit of a conundrum that we face here, which is that… And I'm not sure. We just need to kind of pretty much do a ceremony, right? An actual meeting where we have multiple people with different sets of permissions coming together to perform some sequence of actions in some concerted way.
you play a role in the ceremony, which is not going to be that much fun, I'm sorry. So, the way it works is that, apparently, you installed the GitHub application on our GitHub account, right, for OpenTeometry?
**Trask Stalnaker** 02:12 Okay, I mean, you can also request I think you can request You can try, like… you can… add it and… to the org, and it comes up as a, like, I've been… one of the GitHub org admins has to approve it.
**atoulme** 02:31 I see. So you're saying, hey, maybe there's a workflow we could use here where you approve it, but you're not the installer.
**Trask Stalnaker** 02:37 Yeah.
**atoulme** 02:38 Okay. So here is the choreography that needs to happen somehow, right? So, working you through the steps. Rudiger needs to be the owner, the associated owner of this application to install it.
once that's installed, he needs to have some level of permission around it so that he can set which repositories will be enabled for this particular application. Not all repositories should be enabled, only open time to collector at first, maybe others down the road.
And then he needs to have a handshake with someone on the IBM side, which would look at who is enabling this application, find their IBM ID, because it needs to be an IBM ID person, so I told them Trask is not going to be having that. That's not happening in this timeline.
And so it has to be Rudiger, and he, gave me the name of someone on the end.
who would be responsible for turning that on. The name is Elizabeth Joseph.
So, I end up having to set some sort of either dedicated time or some choreography of this type of things coming together so we can all see, like, did you plug it in? Did you check the box? Did you do the thing, right?
And I'm still losing my mind, because I feel like I'm trying to explain to Rudiger, like, this is not that simple, and Trask is trying to make sure that we're doing a good move on governance, and I invited him a couple times over to this meeting so he could talk to you, because I think I'm just repeating things I'm hearing in. I can infer some of the governance principles of this GitHub account, right? There's just a lot of you don't want to own… you cannot possibly own this personally. There's… we have had that discussion about Gradle, we had all sorts of things like that, so we want to make sure that if it's going to come from a specific vendor for specific integration, it needs to be associated with someone. So he had the SSMD… reflect that already, which is good, that's a good start. Next, we need to make sure that we do this with a proper process, so he gets in there. And then, he needs to be also, and this is a terrible side of it, is that IBM needs to also perform some action on their back, saying someone is asking for access.
Granted, because Rudiger is listed as the owner.
So, what I'm worried about is somehow he installs it, but his IBM ID is no longer associated with him for some reason, and it shows up as Trask, and they can't find the IBM ID, and then we're back to square one, and then we're having another switcheroo discussion.
And I think Rudiger also, he doesn't know, right? We're flat ignorant, thinks that he needs to be admin on the GitHub account for the duration of the authorization protocol so that Elizabeth Joseph can turn that on, but I'm not sure. I hope not.
But it's just a risk that makes me really think this through.
I mean, realistically, by… We're not gonna solve this today, first off. We're not going to solve it next week, because we've got things to do next week, right?
We could try to do it on the show floor if we had excellent Wi-Fi, which has never happened.
So I don't want to set that expectation that we somehow.
**Trask Stalnaker** 05:50 No.
**atoulme** 05:50 time.
So, maybe in 2 weeks, we could try to have this being somewhat coordinated, knowing that Rudiger is out of Germany.
And so the time zones are what they are. I don't even know who Elizabeth Joseph's, would be in our schedule, but just to alleviate any problems and kind of put people in one room for once, I'd love it if we could just organize a meeting, invite you, and maybe Austin, because you're both maintainers of this, so you can take action, whoever from the project in Frasig, right? Someone.
And then have Rudiger and Elizabeth Joseph also invited in some formal meetings, so we can do this and all share screens and see what the other person says, because otherwise I'm gonna be another two months of, like, did you, did you check that thing?
And I'm tired of it.
**Austin Parker** 06:41 Okay, sorry, can you… what exactly are we talking about? I came in late.
**Trask Stalnaker** 06:46 Mainframes.
**atoulme** 06:48 Mainframes. We have a GitHub Action Runner that is only for mainframes that IBM would love to give us access to.
But that requires a fair amount of coordination so that we can add a GitHub application that is going to be tied into the identity of the person adding the application.
That is then validated by the IBM side using their IBM ID, so that they can actually grant access to a mainframe runner that would allow.
**Austin Parker** 07:16 Yeah.
**atoulme** 07:17 The collector in mainframe architectures, which is critical to making sure we.
**Austin Parker** 07:22 You can see.
**atoulme** 07:22 The state says that we support mainframes.
**Austin Parker** 07:25 No, that part makes sense, and the reason this is… Evolve a lot back and forth now, because…
**atoulme** 07:33 Because we are pretty bad at… on the mainframe side, there's just not that much education about, like, some of the intricacies of how to install GitHub applications.
There's also a need for the Guitar application to be installed specifically by Rudiger, because he's got an IBM ID that identifies him as an IBM employee that allows them in the back to turn that on. If it's done by Trask, it won't work. Also, Trask has limited interest in holding and bearing this responsibility.
**Austin Parker** 08:01 No, that, that, right, that part I… I get.
**atoulme** 08:05 My question is more…
**Austin Parker** 08:07 Is the specific sort of access control problem here that we… need that person that has the IBM ID to be, like, an org user?
**atoulme** 08:20 So…
**Austin Parker** 08:20 org admin?
**atoulme** 08:22 I'm worried about this. And I was asking Rudiger about… what I told him is, like, we need to try and give it a good ol' real try here.
And if Trask needs to make you admin for all 5 minutes while IBM is authorizing this, cool, right? Trask can have the button, like, ready, and the moment things are done, poof, pulls you out, and then you're back to normal, and then we're good. But I have no idea.
**Trask Stalnaker** 08:47 And first, I would like to see, because, like, I know we get requests through GitHub.org to install apps, which to me means, like, other people can make the request to install the app, so he might be able to Quote-unquote, install the app, and it will then get queued up as something for us to hit approve on.
**atoulme** 09:10 Okay, potentially that.
**Austin Parker** 09:12 Has this been tried, or not?
**atoulme** 09:13 I think we… No.
**Austin Parker** 09:17 I'm gonna look… I'm looking at the…
**atoulme** 09:20 Yeah, do you see it?
**Austin Parker** 09:20 settings…
**atoulme** 09:22 I haven't seen it.
**Trask Stalnaker** 09:23 No, it's not in the.
**atoulme** 09:25 Okay. It's not a queued up for us.
**Austin Parker** 09:27 Yeah, I always be…
**atoulme** 09:29 Maybe that's that simple, right? Let's try that first, and if it doesn't work, let's do a synchronous meeting where we are able to share screens and see each other's situation.
**Austin Parker** 09:38 Yeah, I feel like that would be the best bet.
**atoulme** 09:41 Okay. Awesome.
**Trask Stalnaker** 09:42 I can do, I can do 7.30… Am Pacific time… Pretty much any day of the week, like, if that, you know…
**Austin Parker** 09:54 see you.
**Trask Stalnaker** 09:54 They're in Germany.
**Austin Parker** 09:55 I see an app on here already.
**atoulme** 09:58 called OBM.
**Austin Parker** 09:59 Yeah.
**atoulme** 10:01 Okay, so if it's installed, who is the, owner of that?
**Austin Parker** 10:05 I'm… I'm checking, I agree.
**atoulme** 10:07 So, Trask might have installed it.
**Austin Parker** 10:09 Power's the GHA runner?
**atoulme** 10:12 Yes.
**Austin Parker** 10:13 Can you share a screen?
Sure. Let me share my screen so you can just see what I'm…
**Trask Stalnaker** 10:19 But yeah, I think you're right, Antoine. I think I did install it, but then the next steps were to… Like, I needed an ID, like, and I was gonna have to own an account. I had to set up an account with them, and I didn't want to do that, so I… yeah, so I suspended it.
**atoulme** 10:40 Because we need to cleanly remove it and have Ridiger try again. Does that sound good?
**Austin Parker** 10:46 Navy, I… well… I'm trying to share. Can you all hear me still?
**atoulme** 10:50 I hear you.
**Austin Parker** 10:52 Okay, my…
**Trask Stalnaker** 10:52 green.
**Austin Parker** 10:53 Yeah, because my Zoom is frozen.
**atoulme** 10:57 Oh, here we go.
**Austin Parker** 10:58 You see it now?
**atoulme** 10:59 You will see some.
**Trask Stalnaker** 11:00 Yeah.
**Austin Parker** 11:01 Okay. Yeah, this is what I see. So… suspended…
**Trask Stalnaker** 11:07 That was me.
**Austin Parker** 11:08 Okay.
**atoulme** 11:09 So, so, so, that's great. Let's… Let's maybe restart there, and…
**Trask Stalnaker** 11:15 uninstall. I like that idea, uninstall it, and…
**Austin Parker** 11:19 Full authorization, IPM ID. Oh, this is it.
This is the thing.
**atoulme** 11:25 That's the issue, right? So, now that we got Rudiger actually officially committed in the SSMD that he's going to own that, let's put it up to it. I can write him a little message on Slack with the steps, but if you would please uninstall the app first. This way, I think that's what's happening, is that he can't move on.
He can't possibly install it if it's already installed, if it's pending.
**Austin Parker** 11:47 Well, I'll uninstall… so we're good at installing this?
**atoulme** 11:50 And then, if he initializes it, maybe he gets more of a say about it, and then we're good to go.
**Austin Parker** 11:57 Yeah, because it should be, because I'm pretty sure, like… I look at this random one.
**atoulme** 12:03 I mean, I don't know, right? I'm not…
**Austin Parker** 12:06 I'm just trying to think who owns…
**Trask Stalnaker** 12:11 Normally, it hasn't mattered.
Right? For the apps, they don't get tied to… Some other account, but this one seems different for some reason, the way that they… their app works.
**Austin Parker** 12:24 Yeah, I'm just trying to… well, cause it… well… But I'm thinking… I'm just trying to remember from installing things, because when you install a GitHub app, it does… Like, you… it does send your email.
I just don't know if it's… the email of the person that approves it, but that… that seems odd. That seems like it wouldn't be…
**atoulme** 12:47 I hope not.
Anyhow.
**Trask Stalnaker** 12:52 Let's try it.
**atoulme** 12:52 Yeah, man.
**Austin Parker** 12:53 Yeah, well, it's uninstalled, so you all can try reinstalling it.
**atoulme** 12:56 Thank you, sir.
Appreciate it.
**Trask Stalnaker** 12:59 Okay. Oh yeah, there was an example of one that was, pending installation requests. At the bottom was Claude.
**Austin Parker** 13:06 Yeah.
**Trask Stalnaker** 13:08 Yeah. But, like, if I click on it, it…
**Austin Parker** 13:10 So I see… also, let me show you what it shows us.
**Trask Stalnaker** 13:15 Yeah, it shows, Puna requested.
**Austin Parker** 13:18 Yeah.
**atoulme** 13:19 Oh, okay, so maybe that is actually going to bind to them In some way. Which is all…
**Austin Parker** 13:25 Do you guess?
I'm…
**Trask Stalnaker** 13:29 Well…
**Austin Parker** 13:30 I guess it has to. I don't care Well, yeah, but I mean, it does… but GitHub does care, because it does, like, ask who installs it, and I'm thinking, like…
**atoulme** 13:39 Yeah.
**Austin Parker** 13:40 like, for Claude, like, this is, you know, it's like, this has to go… this has to hit someone's account, and so I guess it has to hit the account of the person that requested it, right?
**atoulme** 13:48 So you would be paying, for example, for cloud credits?
**Austin Parker** 13:52 a moon?
**atoulme** 13:55 Just put your credit card in there, see what… Help Open Telemetry. Donate your cloud credits.
**Austin Parker** 14:02 Yeah, I don't know.
**atoulme** 14:05 Why not? Okay.
**Austin Parker** 14:06 Well, no, I just, I don't know, I don't know, like, in this case.
**atoulme** 14:10 I don't know… Obviously, it's not the admin of the thing that it's installed into.
Yeah, no, that would be weird too, right? So… Okay, I appreciate it. I have to run, but thank you for helping, and .
**Austin Parker** 14:26 Okay.
**atoulme** 14:27 I'll follow up, and worst case, I'll just put everybody in one room, and we talk, and we figure it out.
**Austin Parker** 14:32 Yeah, that's fine. I mean, I said, I'll be around all next week, assuming.
**atoulme** 14:37 Nice to meet you fly there, yeah.
**Austin Parker** 14:39 Yeah, assuming… Planes don't stop.
I mean, I might, I mean, who knows, I might get there late, but I should be… I will definitely be… in Atlanta next week, one way or the other.
**atoulme** 14:53 Thank you.
**Austin Parker** 14:54 Worst case.
**atoulme** 14:57 Yeah, okay.
**Austin Parker** 15:01 Long road trip to Atlanta, but it's not that bad.
**Trask Stalnaker** 15:05 I'm not driving from Portland.
**Austin Parker** 15:08 That's fair, yeah.
**atoulme** 15:09 We should take a train. We should do, like, a train-based conference.
**Austin Parker** 15:13 I, you know, I wanted to. I… back when…
**atoulme** 15:17 That's… That's super cool.
**Austin Parker** 15:19 when they were gonna do KubeCon, like, the year they were gonna do KubeCon in Boston. It was just the COVID year.
I had a whole thing planned out, where we were gonna rent a… we were gonna do, like, a special train, like, along the eastern seaboard, like, cube… cube train, or something.
Observability train.
**atoulme** 15:42 That would work.
**Trask Stalnaker** 15:42 fun.
**atoulme** 15:44 Right.
**Austin Parker** 15:45 Dias.
**Trask Stalnaker** 15:57 I left… you saw I left comments.
**Austin Parker** 16:00 I do, I'm… I, I will have to… I will get back and look at that.
**Trask Stalnaker** 16:07 But overall, yeah.
**Austin Parker** 16:08 Better.
**Trask Stalnaker** 16:09 I like it, yep.
**Austin Parker** 16:11 Okay, cool.
**Trask Stalnaker** 16:18 Just whenever you have a time to go… Make those updates, or review, then…
**Austin Parker** 16:26 Increase with… Session's invalid, there's no changes. Oh.
Yeah, yeah, I can… Take care of those here in a minute.
Okay, I actually have another meeting… oh, it doesn't start until 2.30, so… I don't have any other, like, info-y things unless we wanted to talk about… Google Groups… But I'm also fine not talking about that right now.
**Trask Stalnaker** 17:07 Yeah.
**Austin Parker** 17:13 Okay, I guess we can call it then.
**Trask Stalnaker** 17:15 Alright.
**Austin Parker** 17:17 Like, how are you?
